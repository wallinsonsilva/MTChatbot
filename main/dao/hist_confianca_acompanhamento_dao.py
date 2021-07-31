import mysql.connector
from main.model.hist_confianca_acompanhamento import HistConfiancaAcompanhamento
from main.model.hist_conf_acom_detalhado import HistConfiancaAcompanhamentoDetlh

class HistConfiancaAcompanhamentoDAO:

    __insert_registro = ("INSERT INTO hist_confianca_acompanhamento (followup_id,confianca) VALUES (%s, %s)")

    __historico_completo = ("SELECT * FROM hist_confianca_acompanhamento")

    __pesquisar_hist_sentenca_id = ("SELECT * FROM hist_confianca_acompanhamento WHERE followup_id = '%s'")

    __pesquisar_hist_completo_sentenca_id = ("SELECT * FROM hist_confianca_acompanhamento"
                                             "WHERE followup_id = '%s'")

    __pesquisar_hist_detalhado_completo= ("SELECT rel.nome_rm, cto.nome_intencao, cto.entrada as 'caso_teste_origem', "
                                          "cta.sentenca as 'caso_teste_acompanhamento', "
                                          "res.seq_resultado, res.resultado_teste, hist.confianca "
                                          "FROM hist_confianca_acompanhamento hist "
                                          "inner join caso_teste_acompanhamento cta "
                                          "on hist.followup_id = cta.sentenca_id "
                                          "inner join caso_teste_origem cto "
                                          "on cto.entrada_id = cta.entrada_id "
                                          "inner join relacoes rel on rel.rm_id = cta.rm_id "
                                          "inner join resultado_teste res "
                                          "on res.sentenca_id = cta.sentenca_id and res.rm_id = cta.rm_id")

    def __init__(self, conn_banco: mysql.connector.connection.MySQLConnection):
        self.conn_banco = conn_banco

    def add_novo_registro(self, registro: HistConfiancaAcompanhamento):
        cursor = self.conn_banco.cursor()
        cursor.execute(self.__insert_registro ,(registro.followup_id, registro.confianca))
        aux = cursor.lastrowid
        cursor.close()
        return aux

    def get_historico_simples(self):
        return self.__get_historico_por_(self.__historico_completo, '')

    def get_historico_por_sentenca_id(self, sentenca_id):
        return self.__get_historico_por_(self.__pesquisar_hist_sentenca_id,sentenca_id)

    def get_historico_detalhade_completo(self):
        historico = []
        cursor = self.conn_banco.cursor()
        cursor.execute(self.__pesquisar_hist_detalhado_completo)
        for (nome_intencao,caso_teste_origem,caso_teste_acompanhamento,seq_resultado,resultado_teste,confianca) in cursor:
            historico.append(
                HistConfiancaAcompanhamentoDetlh(nome_intencao,caso_teste_origem,caso_teste_acompanhamento,seq_resultado,resultado_teste,confianca))
        cursor.close()
        return historico

    def __get_historico_por_(self, consulta, criterio):
        historico = []
        cursor = self.conn_banco.cursor()
        cursor.execute(consulta, criterio)
        for (confianca_id,followup_id,confianca) in cursor:
            historico.append(
                HistConfiancaAcompanhamento(confianca_id,followup_id,confianca))
        cursor.close()
        return historico