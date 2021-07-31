import mysql.connector
from main.model.quantidade_sentenca_gerada import QuantidadeSentecaGeradaRM

class QuantidadeSentecaGeradaRMDAO:
    __insert_quantidade = ("INSERT INTO quantidade_sentencas_rm (rm_id,sentenca_id,quantidade_gerada) VALUES (%s,%s,%s)")
    __todos_registros = ("SELECT * FROM quantidade_sentencas_rm")
    __pesquisar_por_rm = ("SELECT * FROM quantidade_sentencas_rm WHERE rm_id = '%s'")
    __pesquisar_por_sentenca= ("SELECT * FROM quantidade_sentencas_rm WHERE sentenca_id = '%s'")
    __pesquisar_rm_sentenca = ("SELECT * FROM quantidade_sentencas_rm WHERE rm_id = '%s' AND sentenca_id = '%s'")

    def __init__(self, conn_banco:mysql.connector.connection.MySQLConnection):
        self.conn_banco = conn_banco

    def add_quantidade(self, registro: QuantidadeSentecaGeradaRM):
        cursor = self.conn_banco.cursor()
        cursor.execute(self.__insert_quantidade, (registro.rm_id, registro.sentenca_id, registro.quantidade_gerada))
        aux = cursor.lastrowid
        cursor.close()
        return aux

    def get_todos_registros(self):
        return self.__get_entrada_por_(self.__todos_registros, '')

    def pesquisar_por_rm(self, rm_id):
        return self.__get_entrada_por_(self.__pesquisar_por_rm,rm_id)

    def pesquisar_por_sentenca(self, sentenca_id):
        return self.__get_entrada_por_(self.__pesquisar_por_rm,sentenca_id)

    def pesquisar_por_rm_e_sentenca(self, rm_id, sentenca_id):
        return self.__get_entrada_por_(self.__pesquisar_rm_sentenca, (rm_id,sentenca_id))

    def __get_entrada_por_(self, consulta, criterio):
        entradas = []
        cursor = self.conn_banco.cursor()
        cursor.execute(consulta, criterio)
        print(cursor.column_names)
        for (id,rm_id,sentenca_id,quantidade_gerada) in cursor:
            entradas.append(QuantidadeSentecaGeradaRM(id,rm_id,sentenca_id,quantidade_gerada))
        cursor.close()
        return entradas