import spacy
class TrocarLetraLeU:

    def __init__(self):
        self.vogais = ['a', 'á', 'à', 'â', 'ã', 'e', 'é', 'ê', 'i', 'í', 'î', 'o', 'ó', 'ô', 'õ', 'u', 'ú', 'û']
        self.nlp = spacy.load('pt_core_news_md')


    def __prepocessamento_tokens(self,sentenca):
        aux = sentenca.lower();
        doc = self.nlp(aux)
        tokens = [token.text for token in doc]
        return list(tokens)

    def __substituir_palavra(self, sentenca, palavra, substituicao):
        index = sentenca.index(palavra)
        tmp = sentenca.copy()
        tmp[index] = substituicao
        return ' '.join(tmp) \
            .replace(' ,', ',') \
            .replace(' .', '.') \
            .replace(' :', ':') \
            .replace(' ?', '?') \
            .replace(' !', '!')

    # Ex: enfase, teimoso, subsidio
    def __trocar_l_to_u(self, palavra):
        temp = []
        tamanho = len(palavra)
        for i in range(0, tamanho):
            if i!=0 and palavra[i] == 'l':
                if palavra[i - 1] in self.vogais and not palavra[i + 1] in self.vogais:
                    temp.append('u')
                    return ''.join(temp + list(palavra)[i + 1:])
                elif i == (tamanho - 1):
                    temp.append('u')
                    return ''.join(temp + list(palavra)[i + 1:])
                else:
                    temp.append(palavra[i])
            else:
                temp.append(palavra[i])
        return ''.join(temp)

    # Ex: enfase, teimoso, subsidio ()=> enfaze, teimozo, subzidio
    def trocar_L_to_U(self, sentenca):

        sentenca = self.__prepocessamento_tokens(sentenca)
        versoes_sentenca = []

        for s in sentenca:
            if 'l' in s:
                substituicao = self.__trocar_l_to_u(s)
                if substituicao[-1] == 'l':
                    temp = list(substituicao)
                    temp[len(temp)-1] = 'u'
                    substituicao = ''.join(temp)
                print(substituicao)
                versoes_sentenca.append(self.__substituir_palavra(sentenca, s, substituicao))
        return versoes_sentenca