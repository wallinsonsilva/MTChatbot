from main.model.caso_teste_origem import SourceTestCase
from main.model.reposta_resultado_teste import RespostaResultadoTeste
from main.dao.reposta_caso_teste_origem_dao import RespostaCasoTesteOrigemDAO
import mysql.connector

class SourceTestCaseDAO:

    __insert_entrada = ("INSERT INTO caso_teste_origem (entrada,nome_intencao) VALUES (%s, %s)")
    __insert_entrada_derivada = ("INSERT INTO caso_teste_origem (entrada,nome_intencao,derivada_rm,id_rm_derivada) VALUES (%s, %s, %s, %s, %s)")
    __todas_entradas = ("SELECT * FROM caso_teste_origem")
    __pesquisar_entradas_sentenca = ("SELECT * FROM caso_teste_origem WHERE entrada like '%{0}%'")
    __pesquisar_entradas_derivadas = ("SELECT * FROM caso_teste_origem WHERE derivada_rm = 0 AND id_rm_derivada = '%s'")

    def __init__(self, conn_banco:mysql.connector.connection.MySQLConnection):
        self.conn_banco = conn_banco

    # Tupla de ddos ('Resposta','Aplicação')
    def add_entrada(self, entrada:SourceTestCase):
        cursor = self.conn_banco.cursor()
        if entrada.id_rm_derivada == None:
            cursor.execute(self.__insert_entrada,(entrada.entrada,entrada.nome_intencao))
        else:
            cursor.execute(self.__insert_entrada, (entrada.entrada, entrada.nome_intencao, entrada.derivada_rm, entrada.id_rm_derivada))
        aux = cursor.lastrowid
        for res in entrada.respostas:
            RespostaCasoTesteOrigemDAO(self.conn_banco).add_nova_resposta(aux,res)
        cursor.close()
        return aux

    def get_casos_testes(self):
        return self.__get_entrada_por_(self.__todas_entradas,'')

    def pesquisar_caso_teste_sentenca(self, sentenca):
        return self.__get_entrada_por_(self.__pesquisar_entradas_sentenca.format(sentenca),'')

    def pesquisar_caso_teste_derivado_rm(self, rm_id):
        return self.__get_entrada_por_(self.__pesquisar_entradas_derivadas,(rm_id))


    def __get_entrada_por_(self, consulta, criterio):
        entradas = []
        cursor = self.conn_banco.cursor()
        cursor.execute(consulta, criterio)
        for (entrada_id, nome_intencao, entrada,derivada_rm, id_rm_derivada) in cursor:
            entradas.append(SourceTestCase(entrada_id, nome_intencao, entrada, derivada_rm, id_rm_derivada))
        cursor.close()
        return entradas