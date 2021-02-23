from flask import Flask, request
from flask_restful import  Api
import json
from main.SubstanticosSenteca import AnaliseSentenca
from main.SubstituicoesPalavras.SinonimoAntonimo import Search


app = Flask(__name__)
api = Api(app)
analise = None

@app.route("/analise", methods=['POST'])
def analise_sentenca():
    sentenca = request.data.decode('utf-8')
    sentenca = json.loads(sentenca)
    return analise.analise_sintatica(sentenca["sentenca"]).__str__()

@app.route("/extrair_substantivos", methods=['POST'])
def extrair_substantivos():
    sentenca = request.data.decode('utf8')
    sentenca = json.loads(sentenca)
    return analise.extrair_substantivos(sentenca["sentenca"]).__str__()

@app.route("/sinonimo/<palavra>", methods=['GET'])
def sinonimo(palavra):
    resultado = Search(palavra).sinonimo()
    return "{" + resultado.__str__() + "}"

@app.route("/antonimo/<palavra>", methods=['GET'])
def antonimo(palavra):
    resultado = Search(palavra).antonimo()
    return "{"+resultado.__str__() +"}"


if __name__ == '__main__':
    print("Inicializando Analisador")
    analise = AnaliseSentenca()
    print("Inicializando API")
    app.run(port='8000')