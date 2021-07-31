from main.model.resultado_teste import Resultado
from main.model.resultado_completo import ResultadoCompleto
from main.dao.reposta_resultado_teste_dao import RespostaCasoTesteOrigemDAO
import mysql.connector

class ResultadoTesteDAO:

    __insert_resultado = ("INSERT INTO resultado_teste (sentenca_id,rm_id,seq_resultado,resultado_teste ) "
                     "VALUES (%s, %s, %s, %s)")

    __todos_resultados = ("SELECT * FROM resultado_teste")

    __pesquisar_resultado_rm = ("SELECT r.nome_rm, cta.sentenca, rt.seq_resultado, rt.resultado_teste, cto.entrada "
                                "FROM resultado_teste rt "
                                "inner join relacoes r on rt.rm_id = r.rm_id "
                                "inner join caso_teste_acompanhamento cta on rt.sentenca_id = cta.sentenca_id "
                                "inner join caso_teste_origem cto on cto.entrada_id = cta.entrada_id WHERE r.nome_rm like '%{0}%'")



    __pesquisar_resultado_rm_e_sentenca_id = ("SELECT r.nome_rm, cta.sentenca, rt.seq_resultado, rt.resultado_teste, cto.entrada "
                                           "FROM resultado_teste rt "
                                           "inner join relacoes r on rt.rm_id = r.rm_id "
                                           "inner join caso_teste_acompanhamento cta on rt.sentenca_id = cta.sentenca_id "
                                           "inner join caso_teste_origem cto on cto.entrada_id = cto.entrada_id "
                                           "WHERE r.rm_id = '%s' AND cta.sentenca_id = '%s'")

    __pesquisar_resultado_rm_e_sentenca_texto = ("SELECT r.nome_rm, cta.sentenca, rt.seq_resultado, rt.resultado_teste, cto.entrada "
                                           "FROM resultado_teste rt "
                                           "inner join relacoes r on rt.rm_id = r.rm_id "
                                           "inner join caso_teste_acompanhamento cta "
                                           "on rt.sentenca_id = cta.sentenca_id AND cta.rm_id = r.rm_id "
                                           "inner join caso_teste_origem cto on cto.entrada_id = cta.entrada_id "
                                           "WHERE r.nome_rm LIKE '%{0}%' AND cto.entrada LIKE '%{1}%'")

    __pesquisar_ultima_execucao_sentenca = ("SELECT MAX(rt.seq_resultado) "
                                              "FROM resultado_teste rt "
                                              "WHERE rt.sentenca_id = '%s' AND rt.rm_id = '%s'")

    def __init__(self, conn_banco: mysql.connector.connection.MySQLConnection):
        self.conn_banco = conn_banco

    # Tupla de dados ('sentenca_id','rm_id','sequencia', 'resultado_teste')
    def add_resultado(self, resultado: Resultado):
        #Incrementar a sequencia
        sequencia = self.get_ultimo_resultado(resultado.sentenca_id,resultado.rm_id) + 1
        tupla_dados = (resultado.sentenca_id,resultado.rm_id,sequencia,resultado.resultado_teste)
        cursor = self.conn_banco.cursor()
        cursor.execute(self.__insert_resultado, tupla_dados)
        aux = cursor.lastrowid
        for res in resultado.respostas_app:
            RespostaCasoTesteOrigemDAO(self.conn_banco).add_nova_resposta(aux,res)
        cursor.close()
        return aux

    def get_resultados(self):
        return self.__get_relacao_por_(self.__todos_resultados, '')

    def get_resultado_por_rm(self,nome_rm):
        resultados = []
        cursor = self.conn_banco.cursor()
        cursor.execute(self.__pesquisar_resultado_rm.format(nome_rm.upper()),'')
        for (nome_rm,sentenca,seq_resultado,resultado_teste,entrada) in cursor:
            resultados.append(ResultadoCompleto(nome_rm,sentenca,seq_resultado,resultado_teste,entrada))
        return resultados

    def get_resultado_por_rm_e_sentenca_id(self, rm_id, sentenca_id):
        resultados = []
        cursor = self.conn_banco.cursor()
        cursor.execute(self.__pesquisar_resultado_rm_e_sentenca_id, (rm_id, sentenca_id))
        for (nome_rm,sentenca,seq_resultado,resultado_teste,entrada) in cursor:
            resultados.append(ResultadoCompleto(nome_rm,sentenca,seq_resultado,resultado_teste,entrada))
        cursor.close()
        return resultados

    def get_resultado_por_rm_e_sentenca_texto(self, nome_rm, sentenca):
        resultados = []
        cursor = self.conn_banco.cursor()
        cursor.execute(self.__pesquisar_resultado_rm_e_sentenca_texto.format(nome_rm, sentenca),'')
        for (nome_rm,sentenca,seq_resultado,resultado_teste,entrada) in cursor:
            resultados.append(ResultadoCompleto(nome_rm,sentenca,seq_resultado,resultado_teste,entrada))
        cursor.close()
        return resultados

    def get_ultimo_resultado(self,sentenca_id,rm_id):
        seq = 0
        cursor = self.conn_banco.cursor()
        cursor.execute(self.__pesquisar_ultima_execucao_sentenca, (sentenca_id,rm_id))
        temp = cursor.next()
        cursor.close()
        seq = temp[0] if temp[0] != None else 0
        return seq

    def __get_relacao_por_(self, consulta, criterio):
        relacoes = []
        cursor = self.conn_banco.cursor()
        cursor.execute(consulta, criterio)
        for (resultado_id, sentenca_id,rm_id, seq_resultado, resultado_teste) in cursor:
            relacoes.append(Resultado(resultado_id=resultado_id,sentenca_id=sentenca_id, rm_id=rm_id,seq_resultado=seq_resultado, resultado_teste=resultado_teste))
        cursor.close()
        return relacoes