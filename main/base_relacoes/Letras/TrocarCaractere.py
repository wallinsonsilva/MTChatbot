import spacy
from unidecode import unidecode

class TrocarCaracteres:
    __teclado = \
        [
            ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-'],
            ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', '´'],
            ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'ç', '~'],
            ['z', 'x', 'c', 'v', 'b', 'n', 'm', ',', '.', ';', ';']
        ]

    def __init__(self):
        self.nlp = spacy.load('pt_core_news_md')

    def __prepocessamento_tokens(self,sentenca):
        aux = sentenca.lower();
        doc = self.nlp(aux)
        tokens = [token.text for token in doc]
        return list(tokens)

    def trocar_caracteres_vizinhos_teclado(self, sentenca):
        versoes = []
        sentenca = self.__prepocessamento_tokens(sentenca)
        for i in range(0, len(sentenca)):
            substituicoes = self.__trocar_caracteres_vizinhos_palavra_teclado(sentenca[i])
            for s in substituicoes:
                temp = sentenca.copy()
                temp[i] = s
                temp = ' '.join(temp).replace(' ,', ',').replace(' .', '.').replace(' :', ':').replace(' ?', '?').replace(' !', '!')
                versoes.append(temp)

        return versoes

    def deletar_caracteres_vizinhos_sentenca(self,sentenca):
        versoes = []
        sentenca = self.__prepocessamento_tokens(sentenca)
        for i in range(0, len(sentenca)):
            substituicoes = self.__deletar_caractere_palavra(sentenca[i])
            for s in substituicoes:
                temp = sentenca.copy()
                temp[i] = s
                temp = ' '.join(temp).replace(' ,', ',').replace(' .', '.').replace(' :', ':').replace(' ?', '?').replace(' !', '!')
                versoes.append(temp)

        return versoes

    # def deletar_caracteres_vizinhos_sentenca(self,sentenca):
    #     versoes = []
    #     sentenca = self.__prepocessamento_tokens(sentenca)
    #     for i in range(0, len(sentenca)):
    #         substituicoes = self.__deletar_caractere_palavra(sentenca[i])
    #         for s in substituicoes:
    #             temp = sentenca.copy()
    #             temp[i] = s
    #             temp = ' '.join(temp).replace(' ,', ',').replace(' .', '.').replace(' :', ':').replace(' ?', '?').replace(' !', '!')
    #             versoes.append(temp)
    #
    #     return versoes
    #
    def trocar_caracteres_vizinhos_palavra(self,sentenca):
        versoes = []
        sentenca = self.__prepocessamento_tokens(sentenca)
        for i in range(0, len(sentenca)):
            substituicoes = self.__trocar_ordem_caractere_palavra(sentenca[i])
            for s in substituicoes:
                temp = sentenca.copy()
                temp[i] = s
                temp = ' '.join(temp).replace(' ,', ',').replace(' .', '.').replace(' :', ':').replace(' ?', '?').replace(' !', '!')
                versoes.append(temp)

        return versoes

    # Troca os caracteres das palvras por caracteres vizinhos no teclado.
    # A substituição só é feita em palavras com 3 ou mais caracteres
    def __trocar_caracteres_vizinhos_palavra_teclado(self, palavra):
        versoes = []
        if len(palavra) > 2:
            palavra = unidecode(palavra)
            lista_letras_palavra = list(palavra)
            for i in range(0, len(palavra)):
                letra = lista_letras_palavra[i]
                codernadas = self.__buscar_letra_teclado(letra)
                cord_vizinhos = self.__cordenadas_vizinhos(codernadas)
                letras_p_substituicao = self.__letras_por_cordenadas(cord_vizinhos)
                for l in letras_p_substituicao:
                    temp = lista_letras_palavra.copy()
                    temp[i] = l
                    versoes.append(''.join(temp))
        return versoes

    def __deletar_caractere_palavra(self,palavra):
        versoes = []
        if len(palavra) > 4:
            palavra = unidecode(palavra)
            lista_letras_palavra = list(palavra)
            for i in range(1, len(palavra)):
                temp = lista_letras_palavra.copy()
                temp.pop(i)
                versoes.append(''.join(temp))
        return versoes

    def __trocar_ordem_caractere_palavra(self,palavra):
        versoes = []
        if len(palavra) > 4:
            palavra = unidecode(palavra)
            lista_letras_palavra = list(palavra)
            for i in range(0, len(palavra)-1):
                temp = lista_letras_palavra.copy()
                l1 = temp[i]
                l2 = temp[i+1]
                temp[i] = l2
                temp[i+1] = l1
                versoes.append(''.join(temp))
        return versoes


    def __buscar_letra_teclado(self, letra):
        letra = letra.lower()
        for i in range(0, len(self.__teclado)):
            if self.__teclado[i].__contains__(letra):
                return [i, self.__teclado[i].index(letra)]

    def __cordenadas_vizinhos(self,cordenadas):
        x = cordenadas[0]
        y = cordenadas[1]
        dimensao_teclado_x = 3
        dimensao_teclado_y = 10
        vizinhos = []

        if x == 0 and y == 0:
            vizinhos.append([x, y + 1])
            vizinhos.append([x + 1, y])
        elif x == 0 and y > 0 and y < dimensao_teclado_y:
            vizinhos.append([x, y - 1])
            vizinhos.append([x, y + 1])
            vizinhos.append([x + 1, y])
        elif x == 0 and y == dimensao_teclado_y:
            vizinhos.append([x, y - 1])
            vizinhos.append([x + 1, y])
        elif x == dimensao_teclado_x and y == 0:
            vizinhos.append([x - 1, y])
            vizinhos.append([x, y + 1])
        elif x == dimensao_teclado_x and y > 0 and y < dimensao_teclado_y:
            vizinhos.append([x, y - 1])
            vizinhos.append([x, y + 1])
            vizinhos.append([x - 1, y])
        elif x == dimensao_teclado_x and y == dimensao_teclado_y:
            vizinhos.append([x, y - 1])
            vizinhos.append([x + 1, y])
        elif x > 0 and x < dimensao_teclado_x and y > 0 and y < dimensao_teclado_y:
            vizinhos.append([x, y - 1])
            vizinhos.append([x, y + 1])
            vizinhos.append([x - 1, y])
            vizinhos.append([x + 1, y])
        elif x > 0 and y == 0:
            vizinhos.append([x - 1, y])
            vizinhos.append([x, y + 1])
            vizinhos.append([x + 1, y])
        elif x > 0 and y == dimensao_teclado_y:
            vizinhos.append([x - 1, y])
            vizinhos.append([x, y - 1])
            vizinhos.append([x + 1, y])

        return vizinhos

    def __letras_por_cordenadas(self,cordenadas):
        letras = []
        for cor in cordenadas:
            letras.append(self.__teclado[cor[0]][cor[1]])
        return letras