from main.base_relacoes.SubstituicoesPalavras.Tradutor import Tradutor


class RM35_VersoesTraducao:

    def __init__(self,quantidade_treads:3,atraso_tradutor=1):
        self.__tradutor = Tradutor(quantidade_treads,atraso_tradutor)

    def versoes_sentenca_por_traducao(self,senteca):
        return self.__tradutor.versoes_sentencas_traduzidas(senteca)