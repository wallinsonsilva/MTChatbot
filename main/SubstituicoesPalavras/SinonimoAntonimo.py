import requests
from scrapy.selector import Selector as scp
from unicodedata import normalize

class Search(object):

    __host_sinonimo = 'https://www.sinonimos.com.br/{}/'
    __host_antonimo = 'https://www.antonimos.com.br/{}/'

    def __init__(self, palavra):
        super(Search, self).__init__()
        self.word = palavra.split(" ")


    def sinonimo(self, verbose=False):
        param = "-".join(self.word)
        param = normalize('NFKD', param).encode('ASCII', 'ignore').decode('ASCII')
        print("Carregando sinônimos para '{}'...".format(param))
        try:
            r = requests.get(self.__host_sinonimo.format(param))
            print(r)
            if r.status_code == 200:
                conteudo = r.content.decode('iso8859-1')
                sinonimos = scp(text=conteudo).xpath('//a[@class="sinonimo"]/text()').extract()
                return sinonimos
            else:
                return "[]"
        except Exception as e:
            return "Impossivel conectar a internet. :/. Tipo de erro: {}".format(e)


    def antonimo(self):
        param = "-".join(self.word)
        param = normalize('NFKD', param).encode('ASCII', 'ignore').decode('ASCII')
        print("Carregando antônimo para '{}'...".format(param))
        try:
            r = requests.get(self.__host_antonimo.format(param))
            print(r)
            if r.status_code == 200:
                conteudo = r.content.decode('utf-8')
                antonimos = scp(text=conteudo).xpath('//p[@class="antonimos"]/a/text()').extract()
                return antonimos
            else:
                return "[]"
        except Exception as e:
            return "Impossivel conectar a internet. :/. Tipo de erro: {}".format(e)