import nltk
nltk.download('mac_morpho', quiet=True)

class AnaliseSentenca():

    def __init__(self):
        self.__tagged_sents = nltk.corpus.mac_morpho.tagged_sents()
        self.__unigram_tagger = nltk.tag.UnigramTagger(self.__tagged_sents)
        # self.t0 = nltk.tag.DefaultTagger(self.__tag_mais_utilizada())
        self.t1 = nltk.UnigramTagger(self.__tagged_sents)
        self.t2 = nltk.BigramTagger(self.__tagged_sents, backoff=self.t1)
        self.t3 = nltk.TrigramTagger(self.__tagged_sents, backoff=self.t2)


    def __tag_mais_utilizada(self):
        tags = [tag for (word, tag) in nltk.corpus.mac_morpho.tagged_words()]
        return nltk.FreqDist(tags).max()


    def analise_sintatica(self, sentenca):
        tokens = nltk.word_tokenize(sentenca)
        # return self.__unigram_tagger.tag(tokens)
        return self.t3.tag(tokens)

    def extrair_substantivos(self,sentenca):
        tokens = nltk.word_tokenize(sentenca)
        lista_tokens = self.t3.tag(tokens)
        substantivos = []
        for token in lista_tokens:
            if token[1] == 'N':
                substantivos.append(token[0])
        return substantivos

