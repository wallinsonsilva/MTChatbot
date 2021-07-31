from main.model.reposta_caso_teste_origem import RespostaCasoTesteOrigem
import mysql.connector

class RespostaCasoTesteOrigemDAO:

    def __init__(self, conn_banco:mysql.connector.connection.MySQLConnection):
        self.conn_banco = conn_banco

    __add_resposta = ("INSERT INTO resposta_caso_teste_origem (entrada_id,resposta_app) VALUES (%s, %s)")
    __resposta_por_id_entrada = ("SELECT * FROM resposta_caso_teste_origem WHERE entrada_id = %s")

    def add_nova_resposta(self, entrada_id, resposta_app):
        cursor = self.conn_banco.cursor()
        cursor.execute(self.__add_resposta, (entrada_id, resposta_app))
        aux = cursor.lastrowid
        cursor.close()
        return aux

    def get_resposta_por_id_entrada(self,entrada_id):
        cursor = self.conn_banco.cursor()
        cursor.execute(self.__resposta_por_id_entrada,entrada_id)
        respostas = []
        for (id,entrada_id,resposta_app) in cursor:
            respostas.append(RespostaCasoTesteOrigem(id,entrada_id,resposta_app))
        cursor.close()
        return respostas