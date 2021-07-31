import mysql.connector
from main.model.caso_teste_acompanhamento import FollowUpTestCase

class NovasSentencasDAO:

    __insert_sentenca = ("INSERT INTO caso_teste_acompanhamento (rm_id,entrada_id,sentenca) VALUES (%s, %s, %s)")

    __todas_sentenca = ("SELECT * FROM caso_teste_acompanhamento")

    __pesquisar_sentenca_rm = ("SELECT cta.rm_id, r.nome_rm, cta.sentenca_id, cta.sentenca "
                             "FROM caso_teste_acompanhamento cta "
                             "inner join relacoes r on cta.rm_id = r.rm_id "
                             "WHERE r.nome_rm like '%{0}%'")

    __pesquisar_sentenca_caso_teste_inicial = ("SELECT cta.rm_id , r.nome_rm, cta.sentenca, cta.sentenca_id "
                             "FROM caso_teste_acompanhamento cta "
                             "inner join relacoes r on cta.rm_id = r.rm_id "
                             "inner join caso_teste_origem cto on cto.entrada_id = cta.entrada_id "
                             "WHERE cto.entrada like '%{0}%'")

    def __init__(self, conn_banco:mysql.connector.connection.MySQLConnection):
        self.conn_banco = conn_banco

    # Tupla de dados ('rm_id','entrada_id','sentenca')
    def add_nova_sentenca(self, test_case: FollowUpTestCase):
        cursor = self.conn_banco.cursor()
        cursor.execute(self.__insert_sentenca, (test_case.rm_id,test_case.entrada_id,test_case.sentenca))
        aux = cursor.lastrowid
        cursor.close()
        return aux

    def get_sentencas(self):
        return self.__get_relacao_por_(self.__todas_sentenca,'')

    def get_sentenca_por_nome_rm(self, nome_rm):
        relacoes = []
        cursor = self.conn_banco.cursor()
        cursor.execute(self.__pesquisar_sentenca_rm.format(nome_rm.upper()), '')
        for (rm_id, nome_rm, sentenca_id, sentenca) in cursor:
            relacoes.append(FollowUpTestCase(rm_id=rm_id, nome_rm=nome_rm, sentenca_id=sentenca_id, sentenca=sentenca))
        cursor.close()
        return relacoes

    def get_sentenca_por_nome_ct_origem(self, sentenca_caso_teste_origem):
        relacoes = []
        cursor = self.conn_banco.cursor()
        cursor.execute(self.__pesquisar_sentenca_caso_teste_inicial.format(sentenca_caso_teste_origem), '')
        for (rm_id,nome_rm,sentenca_id,sentenca) in cursor:
            relacoes.append(FollowUpTestCase(rm_id=rm_id, nome_rm=nome_rm,sentenca_id=sentenca_id, sentenca=sentenca))
        cursor.close()
        return relacoes

    def __get_relacao_por_(self, consulta, criterio):
        relacoes = []
        cursor = self.conn_banco.cursor()
        cursor.execute(consulta, criterio)
        for (sentenca_id,rm_id,entrada_id,sentenca) in cursor:
            relacoes.append(FollowUpTestCase(sentenca_id=sentenca_id, rm_id=rm_id, entrada_id=entrada_id, sentenca=sentenca))
        cursor.close()
        return relacoes