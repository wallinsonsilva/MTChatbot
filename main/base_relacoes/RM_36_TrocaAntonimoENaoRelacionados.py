from main.SubstituicoesPalavras.Tradutor import Tradutor
from main.SubstituicoesPalavras.ThesaurosRest import ThesaurosRest

class AntonimosENaoRelacionados:

    def __init__(self):
        self.__tradutor = Tradutor(3)
        self.__thesauros = ThesaurosRest()

    # RM3.6
    def rm_36_versoes_antonimo(self,senteca):
        return self.__thesauros.versoes_antonimo(senteca)