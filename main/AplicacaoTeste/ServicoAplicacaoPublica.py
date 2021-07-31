import datetime
import requests
import json
import warnings
warnings.filterwarnings("ignore")
from main.model.mensagem import Mensagem
import datetime

class ServicoAplicacao:

    def __init__(self):

        self.API_URI   = ''
        self.LOGIN_URI = ''
        self.DRAFT_URI = ''
        self.__get_config()
        self.__token = self.__get_token()
        self.__mensagem_inicial()

    def __get_config(self):
        response = requests.get(self.__base_uri + "/config.json", verify=False)
        if response.status_code == 200:
            self.API_URI = response.json()['API_URI']
            self.LOGIN_URI = response.json()['LOGIN_URI']
            self.DRAFT_URI = response.json()['DRAFT_URI']

    def __get_token(self):
        if self.LOGIN_URI != '':
            response_login = requests.get(self.LOGIN_URI + "/oauth2/token", verify=False)
            if response_login.status_code == 200:
                return response_login.json()['access_token']
            return None

    def __mensagem_inicial(self):
        if self.__token != None:
            response_login = requests.get(self.API_URI + "/agentes", verify=False, headers=self.__get_header())
            if response_login.status_code == 200:
                return response_login.json()
            return None



    def enviar_sentenca(self, mensagem, interlocutor):
        if self.__token != None:
            m = Mensagem(mensagem,interlocutor, mensagem)
            response = requests.post(self.__base_uri_mensagem, data=json.dumps(m.__dict__), verify=False,
                                     headers=self.__get_header())
            if response.status_code == 200:
                respostas = []
                for resposta in response.json():
                    respostas.append(resposta['texto'])
                return respostas
            return None
        else:
            return "Token Inválido"
