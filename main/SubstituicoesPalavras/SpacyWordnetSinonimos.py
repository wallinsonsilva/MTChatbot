import spacy
from spacy_wordnet.wordnet_annotator import WordnetAnnotator
from main.SubstituicoesPalavras.Tradutor import Tradutor
import logging
logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%d/%m/%Y %I:%M:%S %p',level=logging.INFO)

class Sinonimo:

    def __init__(self):
        self.__nlp = spacy.load('en_core_web_lg')
        self.__nlp.add_pipe(WordnetAnnotator(self.__nlp.lang), after='tagger')
        self.__domains = ['finance', 'banking', 'betting', 'insurance', 'money', 'commerce']
        self.__lista_elementos_aceitos = ['VERB', 'ADV', 'ADJ', 'NOUN']
        self.__tradutor = Tradutor()

    def sinonimos_elementos(self, sentenca):
        logging.warning('func: sinonimos_elementos')

        sentence = self.__nlp(sentenca)
        sinonimos_token = {}

        for token in sentence:
            if token.pos_ in self.__lista_elementos_aceitos:
                # We get those synsets within the desired domains
                conjunto_sinonimos = token._.wordnet.wordnet_synsets_for_domain(self.__domains)
                sinonimos = []
                for s in conjunto_sinonimos:
                    for l in s.lemma_names():
                        sinonimos.extend([l])
                sinonimos.append(token.text)
                sinonimos_token[token.text] = list(set(sinonimos))

        return sinonimos_token


    #Caso seja passado deep = 0, será feito apenas uma substituição por sentença,
    #caso contrário, será combinado todas as versões possíveis.
    def versoes_sentenca(self,sentenca,deep=0):
        logging.warning('func: versoes_sentenca')

        sentenca = self.__tradutor.traduzir_sentenca_simples(sentenca,'en')
        self.__dic_sinonimos = self.sinonimos_elementos(sentenca)
        sentence = self.__nlp(sentenca)
        versoes = []

        if deep == 0:
            logging.warning('versoes_sentenca[ sentenca: {0}, deep: {1}]'.format(sentenca,deep))
            for sin in self.__dic_sinonimos:
                versoes = versoes + self.__substituir_sinonimos_sentenca(sentence,sin)
                versoes = self.__remover_underline_sentencas(versoes)
                return self.__tradutor.traduzir_sentencas(versoes)
            return versoes
        else:
            logging.warning('versoes_sentenca[ sentenca: {0}, deep: {1}]'.format(sentenca,deep))
            versoes = self.__substituir_sininonimos_profundidade(sentence, self.__dic_sinonimos)
            versoes = self.__remover_underline_sentencas(list(set(versoes)))
            logging.warning('versoes_sentenca[ sentenca: {0}, deep: {1}, len(versoes): {2}]'.format(sentenca, deep, len(versoes)))
            return self.__tradutor.traduzir_sentencas(versoes)


    def __substituir_sinonimos_sentenca(self,sentence:spacy.tokens.doc.Doc,sinonimo_chave:str):
        logging.warning('func: __substituir_sinonimos_sentenca: sinonimo [{0}]'.format(sinonimo_chave))

        versoes = []
        lista_tokens = [token.text for token in sentence]

        for pos_token in range(0, len(sentence)):
            if sentence[pos_token].text == sinonimo_chave and sentence[pos_token].pos_ in self.__lista_elementos_aceitos:
                for s in self.__dic_sinonimos[sinonimo_chave]:
                    temp = lista_tokens.copy()
                    temp[pos_token] = s
                    versoes.append(self.__nova_sentenca(temp))
        return versoes


    def __nova_sentenca(self,sentenca):
        tmp = sentenca.copy()
        return ' '.join(tmp) \
            .replace(' ,', ',') \
            .replace(' .', '.') \
            .replace(' :', ':') \
            .replace(' ?', '?') \
            .replace(' !', '!')

    def __substituir_sininonimos_profundidade(self, sentenca, dic_sinonimos:dict):
        dicionario = dic_sinonimos.copy()
        versoes = []
        if len(dic_sinonimos.keys())>1:
            sin = list(dicionario.keys())[0]
            versoes = versoes + self.__substituir_sinonimos_sentenca(sentenca, sin)
            for v in versoes:
                sentence = self.__nlp(v)
                conjunto_sinonimos = dicionario.get(sin)
                del dicionario[sin]
                versoes = versoes + self.__substituir_sininonimos_profundidade(sentence, dicionario)
                dicionario[sin] = conjunto_sinonimos
        else:
            return self.__substituir_sinonimos_sentenca(sentenca, list(dicionario.keys())[0])
        return versoes

    def __remover_underline_sentencas(self, sentencas):
        versoes = []
        for s in sentencas:
            versoes.append(s.replace('_',' '))
        return versoes