from main.SubstituicoesPalavras.Tradutor import Tradutor
from main.SubstituicoesPalavras.ThesaurosRest import ThesaurosRest
from main.SubstituicoesPalavras.SpacyWordnetSinonimos import Sinonimo

class Sinonimos:

    def __init__(self):
        self.__tradutor = Tradutor(3)
        self.__thesauros = ThesaurosRest()
        self.__sinonimos = Sinonimo()

    def rm_37_versoes_sentenca_por_thesauros(self,senteca):
        return self.__thesauros.versoes_sinonimo(senteca)

    def rm_37_versoes_sentenca_por_spacy_wordnet(self,senteca):
        return self.__sinonimos.versoes_sentenca(senteca,1)

    def rm_37_versoes_sentenca_por_traducao_e_spacy_wordnet(self,senteca):
        novas_versoes = []
        versoes_traduzidas = self.versoes_sentenca_por_traducao(senteca)
        for v in versoes_traduzidas:
            novas_versoes.extend(self.__sinonimos.versoes_sentenca(senteca,1))
        return novas_versoes