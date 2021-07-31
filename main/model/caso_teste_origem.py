from main.model.reposta_caso_teste_origem import RespostaCasoTesteOrigem

class SourceTestCase:

    def __init__(self, entrada_id=0, nome_intencao='', respostas = [], entrada='', derivada_rm=0,id_rm_derivada=None):
        self.entrada_id = entrada_id
        self.nome_intencao = nome_intencao
        self.entrada = entrada
        self.respostas = respostas
        self.derivada_rm = derivada_rm
        self.id_rm_derivada = id_rm_derivada