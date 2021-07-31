from main.base_relacoes.SubstituicoesPalavras.RemoverElementosNaoChave import RemoverElementosNaoChave

class RM_34_RemoverElementos:
    def rm_34_remover_elementos(self,sentenca):
        r = RemoverElementosNaoChave()
        return r.remover_elementos_sintaticos_sentenca(sentenca)