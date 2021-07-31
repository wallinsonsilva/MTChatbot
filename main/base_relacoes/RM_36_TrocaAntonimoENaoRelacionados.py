from main.base_relacoes.SubstituicoesPalavras.Tradutor import Tradutor
from main.base_relacoes.SubstituicoesPalavras.ThesaurosRest import ThesaurosRest

class RM_36_AntonimosENaoRelacionados:

    def __init__(self,quantidade_treads:3,atraso_tradutor=1):
        self.__tradutor = Tradutor(quantidade_treads,atraso_tradutor)
        self.__thesauros = ThesaurosRest()

    # RM3.6
    def rm_36_versoes_antonimo(self,senteca):
        return self.__thesauros.versoes_antonimo(senteca)