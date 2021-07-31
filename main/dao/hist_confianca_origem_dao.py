import mysql.connector
from main.model.hist_confianca_origem import HistConfiancaOrigem

class HistConfiancaAcompanhamentoDAO:

    __insert_registro = ("INSERT INTO hist_confianca_origem (entrada_id,confianca) VALUES (%s, %s)")

    __historicos = ("SELECT * FROM hist_confianca_origem")

    __pesquisar_hist_entrada_id = ("SELECT * FROM hist_confianca_origem WHERE entrada_id = '%s'")

    def __init__(self, conn_banco: mysql.connector.connection.MySQLConnection):
        self.conn_banco = conn_banco

    def add_novo_registro(self, registro: HistConfiancaOrigem):
        cursor = self.conn_banco.cursor()
        cursor.execute(self.__insert_registro ,(registro.entrada_id, registro.confianca))
        aux = cursor.lastrowid
        cursor.close()
        return aux

    def get_historico_simples(self):
        return self.__get_historico_por_(self.__historicos, '')

    def get_historico_por_sentenca_id(self, sentenca_id):
        return self.__get_historico_por_(self.__pesquisar_hist_entrada_id,sentenca_id)

    def __get_historico_por_(self, consulta, criterio):
        historico = []
        cursor = self.conn_banco.cursor()
        cursor.execute(consulta, criterio)
        for (confianca_id,entrada_id,confianca) in cursor:
            historico.append(HistConfiancaOrigem(confianca_id,entrada_id,confianca))
        cursor.close()
        return historico