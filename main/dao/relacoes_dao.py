from main.model.relacao import Relacao
import mysql.connector

class RelacoesDAO:

    __insert_relacao = ("INSERT INTO relacoes (nome_rm,observacao) VALUES (%s,%s)")
    __todas_relacoes = ("SELECT * FROM relacoes")
    __pesquisar_relacoes_nome = ("SELECT * FROM relacoes WHERE nome_rm like '%{0}%' LIMIT 1")

    def __init__(self, conn_banco:mysql.connector.connection.MySQLConnection):
        self.conn_banco = conn_banco

    def add_relacao(self, relacao: Relacao):
        cursor = self.conn_banco.cursor()
        cursor.execute(self.__insert_relacao, (relacao.nome_rm.upper(),relacao.observacao))
        aux = cursor.lastrowid
        cursor.close()
        return aux

    def get_relacoes(self):
        return self.__get_relacao_por_(self.__todas_relacoes,'')

    def get_relacao_por_nome(self, nome_rm):
        return self.__get_relacao_por_(self.__pesquisar_relacoes_nome.format(nome_rm.upper()),'')

    def __get_relacao_por_(self, consulta, criterio):
        relacoes = []
        cursor = self.conn_banco.cursor()
        cursor.execute(consulta, criterio)
        for (rm_id,nome_rm,observacao) in cursor:
            relacoes.append(Relacao(rm_id=rm_id,nome_rm=nome_rm,observacao=observacao))
        cursor.close()
        return relacoes