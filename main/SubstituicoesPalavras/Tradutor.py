from google_trans_new import google_translator
from multiprocessing.dummy import Pool as ThreadPool
from functools import partial
import logging
logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%d/%m/%Y %I:%M:%S %p',level=logging.INFO)

class Tradutor:
    # idiomasAbreviados = ['af', 'sq', 'am', 'ar', 'hy', 'az', 'eu', 'be', 'bn', 'bs', 'bg', 'ca', 'ceb', 'zh-CN',
    #                      'zh-TW', 'co', 'hr', 'cs', 'da', 'nl', 'en', 'eo', 'et', 'fi', 'fr', 'fy', 'gl', 'ka', 'de',
    #                      'el', 'gu', 'ht', 'ha', 'haw', 'iw', 'hi', 'hmn', 'hu', 'is', 'ig', 'id', 'ga', 'it', 'ja',
    #                      'jv', 'kn', 'kk', 'km', 'rw', 'ko', 'ku', 'ky', 'lo', 'la', 'lv', 'lt', 'lb', 'mk', 'mg', 'ms',
    #                      'ml', 'mt', 'mi', 'mr', 'mn', 'my', 'ne', 'no', 'ny', 'or', 'ps', 'fa', 'pl', 'pt', 'pa', 'ro',
    #                      'ru', 'sm', 'gd', 'sr', 'st', 'sn', 'sd', 'si', 'sk', 'sl', 'so', 'es', 'su', 'sw', 'sv', 'tl',
    #                      'tg', 'ta', 'tt', 'te', 'th', 'tr', 'tk', 'uk', 'ur', 'ug', 'uz', 'vi', 'cy', 'xh', 'yi', 'yo',
    #                      'zu']

    idiomasAbreviados = ['af', 'sq', 'am', 'ar']

    def __init__(self):
        self.__tradutor = google_translator()
        self.__quantidade_threads = 10

    def versoes_sentencas_traduzidas(self, sentenca):
        resultado = self.__sentencas_traduzidas(sentenca)
        resultado_final = self.__sentencas_distintas(resultado)
        return resultado_final

    def traduzir_sentenca(self, text, idioma):
        try:
            logging.warning('func: traduzir_sentenca | [idioma:{0}]'.format(idioma))
            destino = self.__tradutor.translate(text, lang_tgt=idioma)

            logging.warning('func: traduzir_sentenca | [idioma:{0}]'.format('pt'))
            texto = self.__tradutor.translate(destino, lang_tgt='pt')

            logging.warning('func: traduzir_sentenca | [idioma:{0}]: {1}'.format('pt',texto))
            # Em todas as strings traduzidas e add um espaço, então nesse ponto eu os removo
            return texto[:-1]
        except Exception as e:
            logging.warning('func: traduzir_sentenca | [idioma:{0}]: {1}'.format('pt', 'Falha na tradução'))
            logging.warning(str(e))
            return ''

    def  traduzir_sentencas(self,sentencas:list,idioma='pt'):
        logging.warning('func: traduzir_sentencas')
        versoes = []
        try:
            versoes = self.__sentencas_traduzidas_mt(sentencas,idioma)
            return self.__sentencas_distintas(versoes)
        except:
            return ''

    def  traduzir_sentencas_en(self,sentencas:list):
        logging.warning('func: traduzir_sentencas_en')
        versoes = []
        try:
            versoes = self.__sentencas_traduzidas_mt(sentencas,idioma='en')
            return self.__sentencas_distintas(versoes)
        except:
            return ''


    def traduzir_sentenca_simples(self, text, idioma='pt'):
        logging.warning('func: traduzir_sentenca_simples')
        try:
            texto = self.__tradutor.translate(text, lang_tgt=idioma)
            logging.warning('func: traduzir_sentenca_simples | [idioma:{0}]: {1}'.format('pt', texto))
            return texto
        except:
            logging.warning('func: traduzir_sentenca_simples | [idioma:{0}]: {1}'.format('pt', 'Falha na tradução'))
            return ''



    def traduzir_sentenca_simples_por_idioma(self, text, idioma):
        logging.warning('func: traduzir_sentenca_simples_por_idioma')
        try:
            texto = self.__tradutor.translate(text, lang_tgt=idioma)
            logging.warning('func: traduzir_sentenca_simples_por_idioma | [idioma:{0}]: {1}'.format(idioma, texto))
            # Em todas as strings traduzidas e add um espaço, então nesse ponto eu os removo
            return texto
        except:
            logging.error('func: traduzir_sentenca_simples_por_idioma | [idioma:{0}]: {1}'.format('pt', 'Falha na tradução'))
            return ''

    def __sentencas_distintas(self, sentencas):
        while sentencas.__contains__(''):
            index = sentencas.index('')
            sentencas.pop(index)
        return list(set(sentencas))

    def __sentencas_traduzidas(self,entrada):
        logging.warning('func: __sentencas_traduzidas')
        self.__pool = ThreadPool(10)
        resultado = []
        try:
            func = partial(self.traduzir_sentenca, entrada)
            resultado = self.__pool.map(func, self.idiomasAbreviados)
            logging.warning('func: __sentencas_traduzidas: {0}'.format(resultado))
            self.__pool.close()
            self.__pool.join()
        except:
            return []

        return resultado

    #Traduzir as sentencas usando multi threads
    def __sentencas_traduzidas_mt(self, sentencas, idioma='pt'):
        logging.warning('func: __sentencas_traduzidas_mt')
        self.__pool = ThreadPool(self.__quantidade_threads)
        resultado = []

        if idioma == 'pt':
            try:
                logging.warning('func: __sentencas_traduzidas_mt_pt: {0}'.format(resultado))
                resultado = self.__pool.map(self.__traduzir_sentencas_to_pt, sentencas)
                self.__pool.close()
                self.__pool.join()
            except Exception as e:
                logging.warning('func: __sentencas_traduzidas_mt_pt: except return []')
                logging.warning(str(e))
                return []
            return resultado
        elif idioma == 'en':
            try:
                logging.warning('func: __sentencas_traduzidas_mt_en: {0}'.format(resultado))
                resultado = self.__pool.map(self.__traduzir_sentencas_to_en,sentencas)
                self.__pool.close()
                self.__pool.join()
            except Exception as e:
                logging.warning('func: __sentencas_traduzidas_mt_en: except return []')
                logging.warning(str(e))
                return []
            return resultado
        return []

    def __traduzir_sentencas_to_en(self, text):
        try:
            texto = self.__tradutor.translate(text, lang_tgt='en')
            return texto
        except Exception as e:
            logging.warning('func: __traduzir_sentencas_to_en: except return \'\'')
            logging.warning(str(e))
            return ''

    def __traduzir_sentencas_to_pt(self, text):
        try:
            texto = self.__tradutor.translate(text, lang_tgt='pt')
            return texto
        except Exception as e:
            logging.warning('func: __traduzir_sentencas_to_en: except return \'\'')
            logging.warning(str(e))
            return ''