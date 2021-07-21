from main.SubstituicoesPalavras.Tradutor import Tradutor
from main.SubstituicoesPalavras.ThesaurosRest import ThesaurosRest
from main.SubstituicoesPalavras.SpacyWordnetSinonimos import Sinonimo

class VersoesTraducao:

    def __init__(self):
        self.__tradutor = Tradutor(3)

    def versoes_sentenca_por_traducao(self,senteca):
        return self.__tradutor.versoes_sentencas_traduzidas(senteca)