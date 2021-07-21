import spacy


class NegarSentenca:

    def __init__(self):
        self.__nlp = spacy.load('pt_core_news_lg')

    # RM3.1
    def rm_31_negar(self,sentenca):
        doc = self.__nlp(sentenca)
        tokens = [(token.text,token.pos_) for token in doc]
        sentencas = []
        for elemento in tokens:
            if elemento[1] == 'VERB':
                sentencas.append(sentenca.replace(elemento[0],'não '+elemento[0]))
        return sentencas