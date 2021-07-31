import mysql.connector
from mysql.connector import errorcode

class Banco:

    def getConnection(self):
        return self.__criar_conexao()

    def __criar_conexao(self):
        try:
            con = mysql.connector.connect(user=' root', password='', host='localhost', database='relacoes_metamorficas')
            return con
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)

