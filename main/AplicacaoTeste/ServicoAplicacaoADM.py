import datetime
import requests
import json
import warnings
warnings.filterwarnings("ignore")
from main.model.mensagem_parse import MensagemParse
from main.model.sentenca_aplicacao import Sentenca
import datetime

class ServicoAplicacaoADM:

    def __init__(self,token):

        self.__token = token
        self.all_intents = self.get_all_intencoes()



    def enviar_sentenca_parse(self, mensagem):
        m = MensagemParse(mensagem)
        response = requests.post(self.__base_uri_mensagem+"/mensagens/parse", data=json.dumps(m.__dict__), verify=False,
                                 headers=self.__get_header())
        if response.status_code == 200:
            return response.json()
        return None

    def listar_ultimas_dialogos(self):
        response = requests.get(self.__base_uri_mensagem + "/dialogos/paginada?pagina=0&porPagina=10&order_by=desc",verify=False,headers=self.__get_header())
        if response.status_code == 200:
            return response.json()
        return None

    def get_id_ultimo_dialogo_interlocutor(self, interlocutor):
        response = requests.get(self.__base_uri_mensagem + "/dialogos/paginada?pagina=0&porPagina=10&order_by=desc",verify=False,headers=self.__get_header())
        if response.status_code == 200:
            for res in response.json()['itens']:
                if res['interlocutor'] == interlocutor:
                    return str(res['id'])
        return None

    def listar_intecoes(self):
        response = requests.get(self.__base_uri_mensagem + "/intencoes?ativas=false",verify=False,headers=self.__get_header())
        if response.status_code == 200:
            return response.json()
        return None

    def get_sentenca(self, id_sentenca):
        response = requests.get(self.__base_uri_mensagem + "/dialogos/" + str(id_sentenca) + "?incluirTodos=false", verify=False,
                                headers=self.__get_header())
        if response.status_code == 200:
            dialogos = []
            for sentenca in response.json()['dialogoExemplos']:
                dialogos.append(Sentenca(sentenca['id'], sentenca['idIntencao'], sentenca['texto'], sentenca['confianca']))
            return dialogos
        return None

    def get_all_intencoes(self):
        intencoes = {}
        response = requests.get(self.__base_uri_mensagem + "/intencoes?ativas=false",verify=False,headers=self.__get_header())
        for intent in response.json():
            intencoes[intent['id']] = intent['nome']
        return intencoes

    def atualizar_intencao_sentenca(self, id_sentenca, id_intencao):
        response = requests.put(self.__base_uri_mensagem + "/dialogosexemplos/" + str(id_sentenca), verify=False,
                                headers=self.__get_header(), data=str(id_intencao))
        if response.status_code == 200:
            response = requests.put(self.__base_uri_mensagem + "/dialogosexemplos/" + str(id_sentenca) + "/incluir", verify=False,
                                    headers=self.__get_header())
            if response.status_code == 200:
                return True
        return False
