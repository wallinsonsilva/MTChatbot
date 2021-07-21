import unicodedata
import spacy
from nltk.stem import RSLPStemmer

class TrocarLetraX:
    dicionario_x = \
        {
            'x_ch': ['abacaxi', 'baixo', 'bexiga', 'bruxa', 'caixa', 'compaixão', 'coxinha', 'deixar', 'engraxar',
                     'enxada',
                     'enxaqueca', 'enxergar', 'enxerido', 'enxofre', 'enxugar', 'faxina', 'frouxo', 'lixo', 'luxo',
                     'mexer', 'paixão',
                     'peixaria', 'puxar', 'queixo', 'relaxar', 'roxo', 'trouxa'],

            'x_s': ['exclamação', 'excluído', 'excluir', 'exclusivo', 'excursão', 'expectativa', 'experiência',
                    'experiente',
                    'explicação', 'explicar', 'explícito', 'explodir', 'explorar', 'explosão', 'exposição', 'expressar',
                    'exprimir',
                    'extensão', 'extensível', 'extenso', 'exterior', 'extermínio', 'externo', 'extinção', 'extinguir',
                    'extinto',
                    'extrair', 'extremidade', 'extremo', 'extrovertido', 'sexto', 'têxtil', 'texto', 'textual'],

            'x_z': ['exagerado', 'exagero', 'exaltado', 'exame', 'examinar', 'exasperado', 'exato', 'exaustivo',
                    'exausto',
                    'execrável', 'executar', 'executivo', 'exemplar', 'exemplificar', 'exemplo', 'exequível',
                    'exercício', 'exército',
                    'exibir', 'exigência', 'exigir', 'exilado', 'exílio', 'existência', 'existir', 'êxito', 'êxodo',
                    'exorcizar', 'exótico',
                    'exuberante'],

            'x_cs': ['anexo', 'asfixia', 'axila', 'boxe', 'complexo', 'conexão', 'convexo', 'fixo', 'flexão', 'fluxo',
                     'intoxicação',
                     'látex', 'léxico', 'maxilar', 'nexo', 'ortodoxo', 'óxido', 'oxigênio', 'paradoxo', 'reflexão',
                     'reflexo', 'saxofone',
                     'sexagésimo', 'táxi', 'tóxico', 'toxina'],

            'x_ss': ['aproximação', 'aproximar', 'auxiliador', 'auxiliar', 'auxílio', 'máximo', 'proximidade',
                     'próximo'],

            'x_x': ['exceção', 'excedente', 'exceder', 'excelência', 'excelente', 'excelentíssimo', 'excentricidade',
                    'excêntrico',
                    'excepcional', 'excepcionalidade', 'excerto', 'excessivo', 'excesso', 'exceto', 'excitação',
                    'excitante', 'excitar', 'exsudação']
        }

    def __init__(self):
        self.nlp = spacy.load('pt_core_news_md')
        self.vogais = ['a', 'á', 'à', 'â', 'ã', 'e', 'é', 'ê', 'i', 'í', 'î', 'o', 'ó', 'ô', 'õ', 'u', 'ú', 'û']
        self.stemmer = RSLPStemmer()


    def __normalizar(self,palavra):
        palavra = unicodedata.normalize('NFKD', palavra)
        palavra = palavra.encode('ASCII', 'ignore')
        palavra = palavra.lower()
        return palavra

    def __prepocessamento_tokens(self,sentenca):
        aux = sentenca.lower();
        doc = self.nlp(aux)
        tokens = [token.text for token in doc]
        return list(tokens)

    def __substituir_letra(self,sentenca, palavra, letra, substituicao):
        index = sentenca.index(palavra)
        palavra = palavra.replace(letra, substituicao)
        tmp = sentenca.copy()
        tmp[index] = palavra
        return ' '.join(tmp) \
            .replace(' ,', ',') \
            .replace(' .', '.') \
            .replace(' :', ':') \
            .replace(' ?', '?') \
            .replace(' !', '!')

    def __substituir_palavra(self,sentenca, palavra, substituicao):
        index = sentenca.index(palavra)
        tmp = sentenca.copy()
        tmp[index] = substituicao
        return ' '.join(tmp) \
            .replace(' ,', ',') \
            .replace(' .', '.') \
            .replace(' :', ':') \
            .replace(' ?', '?') \
            .replace(' !', '!')

    def __retornar_dicionario_lematizado(self,dicio):
        dicio_final = {}
        for tipo in dicio.keys():
            list_tipo_temp = []
            for palavra in dicio.get(tipo):
                list_tipo_temp.append(self.stemmer.stem(palavra))
            dicio_final[tipo] = list_tipo_temp

        return dicio_final

    def __buscar_pelo_stem(self,dicionario_stem, palavra):
        for tipo in dicionario_stem.keys():
            for elemento in dicionario_stem.get(tipo):
                if palavra.startswith(elemento):
                    return tipo
        return []

    def __alterar_letra_classificacao(self,palavra, classificacao):
        if classificacao == 'x_ch':
            return palavra.replace('x', 'ch')
        if classificacao == 'x_s':
            return palavra.replace('x', 's')
        if classificacao == 'x_z':
            return palavra.replace('x', 'z')
        if classificacao == 'x_ss':
            return palavra.replace('x', 'ss')
        if classificacao == 'x_x':
            return palavra.replace('x', '')
        if classificacao == 'x_cs':
            return palavra.replace('x', 'cs')

    # Verificar se existe X e troca por CH nas palavras.
    # A comparação ignora o primeiro e o último caractere
    def trocar_x(self, sentenca):
        dicionario_stem = self.__retornar_dicionario_lematizado(self.dicionario_x)
        sentenca = self.__prepocessamento_tokens(sentenca)
        versoes_sentenca = []
        for s in sentenca:
            if 'x' in s and not s.startswith('x') and not s.endswith('x'):
                palavra_stem = self.stemmer.stem(s)
                posicao = s.find('x')
                if posicao != -1:
                    # Verifica se o X tem o som de Z.
                    # Regra: Iniciadas com E seguidas de X e outra Vogal qualquer
                    if posicao == 1 and s[posicao - 1] == 'e' and s[posicao + 1] in self.vogais:
                        versoes_sentenca.append(self.__substituir_letra(sentenca, s, 'x', 'z'))
                        continue
                    # Verifica se o X tem o som de S.
                    # Regra: E + X + Consoante
                    if palavra_stem in dicionario_stem.get('x_s'):
                        versoes_sentenca.append(self.__substituir_letra(sentenca, s, 'x', 's'))
                        continue
                    # Verifica se o X tem o som de SS.
                    # Regra: Vogal + X + Vogal
                    if s[posicao - 1] in self.vogais and s[posicao + 1] in self.vogais:
                        if palavra_stem in dicionario_stem.get('x_ss'):
                            versoes_sentenca.append(self.__substituir_letra(sentenca, s, 'x', 'ss'))
                            continue
                    # Verifica se o X tem o som de CH.
                    if palavra_stem in dicionario_stem.get('x_ch'):
                        versoes_sentenca.append(self.__substituir_letra(sentenca, s, 'x', 'ch'))
                        continue
                    # Verifica se o X tem o som de CS.
                    if palavra_stem in dicionario_stem.get('x_cs'):
                        versoes_sentenca.append(self.__substituir_letra(sentenca, s, 'x', 'cs'))
                        continue
                    # Verifica se o X não tem som.
                    if palavra_stem in dicionario_stem.get('x_x'):
                        versoes_sentenca.append(self.__substituir_letra(sentenca, s, 'x', ''))
                        continue
                    # Pior caso,será feito uma busca levando em conta os radicais do dicionários de stems
                    classificacao = self.__buscar_pelo_stem(dicionario_stem, s)
                    if classificacao != []:
                        palavra = self.__alterar_letra_classificacao(s, classificacao)
                        versoes_sentenca.append(self.__substituir_palavra(sentenca, s, palavra))
                        continue

        return versoes_sentenca


#
#
#
# if __name__ == '__main__' :
#     dicionario_stem = __retornar_dicionario_lematizado(dicionario_x)
#     sentenca = 'conexão excedente exuberante excluíndo caixa'
#     tokens = __prepocessamento_tokens(sentenca)
#     print(trocar_x(tokens,dicionario_stem))