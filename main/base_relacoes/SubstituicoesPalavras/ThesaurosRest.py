import spacy
import requests
import json
from main.base_relacoes.SubstituicoesPalavras.Tradutor import Tradutor

class ThesaurosRest:

    def __init__(self):
        self.__nlp = spacy.load('en_core_web_lg')
        self.__elementos_sintaticos = ['verb', 'adv']
        self.__limiar_substituicao = 50
        self.__tipos = ['synonyms', 'antonyms']
        self.__tradutor = Tradutor(1,1)

    def versoes_sinonimo(self, sentenca):
        return self.__versoes(sentenca,0)

    def versoes_antonimo(self, sentenca):
        return self.__versoes(sentenca,1)

    def __versoes(self,sentenca,tipo):
        sentenca = self.__tradutor.traduzir_sentenca_simples(sentenca, 'en')
        tokens = self.__prepocessamento_tokens(sentenca)
        elementos_troca = self.__selecionar_elementos_sintaticos(tokens)
        # return self.__fazer_substituicoes(elementos_troca, sentenca, tipo)
        return self.__traduzir_sentencas(self.__fazer_substituicoes(elementos_troca, sentenca, tipo))

    def __selecionar_elementos_sintaticos(self,lista_tokens_pos):
        palavras = []
        for elemento in lista_tokens_pos:
            if elemento[1].lower() in self.__elementos_sintaticos:
                palavras.append(elemento)

        return palavras

    def __prepocessamento_tokens(self,sentenca):
        doc = self.__nlp(sentenca)
        tokens = [(token.orth_, token.pos_) for token in doc]
        return tokens

    def __buscar_thesauros(self,palavra):
        response = requests.get('http://www.thesaurus.com/browse/{}'.format(palavra))
        resposta = None
        if response.status_code == 200:
            resposta = response.text
            inicio = resposta.index('"posTabs":[')
            fim = resposta.index(',"relatedWordsApiData')
            resposta = response.text[inicio:fim]
            resposta = '{' + resposta
            resposta = json.loads(resposta)
        return resposta

    # Variaveis: JSON do Thesauros, Part-of-tagging, tipo: sinonimo (0) or antonimo (1)
    def __extrair_sinonimos_or_antonimos(self, thesauros, pos, tipo):
        retorno = []
        tipo_sintatico = self.__tipos[0] if tipo == 0 else self.__tipos[1]
        for i in thesauros['posTabs']:
            if str(i["pos"]).__contains__(pos.lower()):
                print(i["pos"], ":", i["definition"])
                for j in i[tipo_sintatico]:
                    retorno.append((int(j['similarity']), j['term']))

        return retorno

    # Variaveis: JSON do Thesauros, Part-of-tagging, tipo: sinonimo (0) or antonimo (1)
    def __fazer_substituicoes(self,elementos_troca, sentenca, tipo):
        versoes = []
        for e in elementos_troca:
            thesauros = self.__buscar_thesauros(e[0])
            substituicoes = self.__extrair_sinonimos_or_antonimos(thesauros, e[1], tipo)
            for sub in substituicoes:
                if sub[0] >= self.__limiar_substituicao or sub[0] <= (self.__limiar_substituicao * -1):
                    versoes.append(sentenca.replace(e[0], sub[1]))

        return versoes

    def sinonimos(self,palavra,pos):
        thesauros = self.__buscar_thesauros(palavra)
        return self.__extrair_sinonimos_or_antonimos(thesauros, pos, 0)

    def antonimos(self,palavra,pos):
        thesauros = self.__buscar_thesauros(palavra)
        return self.__extrair_sinonimos_or_antonimos(thesauros, pos, 1)

    # def __traduzir_sentencas(self,sentencas):
    #     versoes = []
    #     for s in sentencas:
    #         versoes.append(self.__tradutor.traduzir_sentenca_simples(s,'pt'))
    #     return versoes

    def __traduzir_sentencas(self,sentencas):
        return self.__tradutor.traduzir_sentencas(sentencas)