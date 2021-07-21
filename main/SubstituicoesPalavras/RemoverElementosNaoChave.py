import spacy
from unidecode import unidecode

class RemoverElementosNaoChave:

    def __init__(self):
        self.__nlp = spacy.load('pt_core_news_lg')
        self.__elementos_p_remover = ['DET','CCONJ','SCONJ']


    def __prepocessamento_tokens(self,sentenca):
        doc = self.__nlp(sentenca)
        tokens = [(token.text, token.pos_) for token in doc]
        return tokens

    def __identificar_palavra_classe(self,tokens):
        return [t[0] for t in tokens if t[1] in self.__elementos_p_remover]

    def remover_elementos_sintaticos_sentenca(self, sentenca):
        doc = self.__nlp(sentenca)
        tokens = self.__prepocessamento_tokens(sentenca)
        sentencas = []
        palavras = self.__identificar_palavra_classe(tokens)
        for p in palavras:
            sentencas.append(' '.join([token.text for token in doc if token.text != p]))
        return sentencas
