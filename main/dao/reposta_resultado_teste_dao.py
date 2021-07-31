from main.model.reposta_resultado_teste import RespostaResultadoTeste
import mysql.connector

class RespostaCasoTesteOrigemDAO:

    def __init__(self, conn_banco:mysql.connector.connection.MySQLConnection):
        self.conn_banco = conn_banco

    __add_resposta = ("INSERT INTO resposta_resultado_teste (resultado_id,resposta_app) VALUES (%s, %s)")
    __resposta_por_id_entrada = ("SELECT * FROM resposta_resultado_teste WHERE resultado_id = %s")

    def add_nova_resposta(self, resultado_id,resposta_app):
        cursor = self.conn_banco.cursor()
        cursor.execute(self.__add_resposta, (resultado_id,resposta_app))
        aux = cursor.lastrowid
        cursor.close()
        return aux

    def get_resposta_por_id_entrada(self,entrada_id):
        cursor = self.conn_banco.cursor()
        cursor.execute(self.__resposta_por_id_entrada,entrada_id)
        respostas = []
        for (id,resultado_id,resposta_app) in cursor:
            respostas.append(RespostaResultadoTeste(id,resultado_id,resposta_app))
        cursor.close()
        return respostas