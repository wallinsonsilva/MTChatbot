import spacy
class TrocarLetraSCCedilhaSS:

    def __init__(self):
        self.vogais = ['a', 'á', 'à', 'â', 'ã', 'e', 'é', 'ê', 'i', 'í', 'î', 'o', 'ó', 'ô', 'õ', 'u', 'ú', 'û']
        self.nlp = spacy.load('pt_core_news_md')


    def __prepocessamento_tokens(self,sentenca):
        aux = sentenca.lower();
        doc = self.nlp(aux)
        tokens = [token.text for token in doc]
        return list(tokens)


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


    # Ex: enfase, teimoso, subsidio
    def __trocar_s_to_z(self, palavra):
        temp = []
        for i in range(0,len(palavra)):
            if i!=0 and palavra[i] == 's' and (palavra[i - 1] in self.vogais or palavra[i - 1] == 'b') and palavra[i + 1] in self.vogais:
                temp.append('z')
                return ''.join(temp + list(palavra)[i+1:])
            else:
                temp.append(palavra[i])
        return ''.join(temp)

    def __trocar_s_to_c_cedilha(self, palavra):
        temp = []
        for i in range(0, len(palavra)-1):
            if i!=0 and palavra[i] == 's' and not palavra[i-1] in self.vogais and palavra[i+1] in ['e','é','ê','i','í','î']:
                temp.append('c')
                return ''.join(temp + list(palavra)[i + 1:])
            elif i!=0 and palavra[i] == 's' and not palavra[i-1] in self.vogais and palavra[i+1] in ['a','á','à','â','ã','o','ó','ô','õ','u','ú','û']:
                temp.append('ç')
                return ''.join(temp + list(palavra)[i + 1:])
            else:
                temp.append(palavra[i])
        return ''.join(temp)

    # Ex: enfase, teimoso, subsidio ()=> enfaze, teimozo, subzidio
    def trocar_S_to_Z(self, sentenca):

        sentenca = self.__prepocessamento_tokens(sentenca)
        versoes_sentenca = []

        for s in sentenca:
            if 's' in s and not s.startswith('s'):
                substituicao = self.__trocar_s_to_z(s)
                versoes_sentenca.append(self.__substituir_palavra(sentenca, s,substituicao))
        return versoes_sentenca

    # Ex: acesso, acessório, acessível ()=> aceso, acesorio, acesivel
    def trocar_SS_to_S(self, sentenca):
        sentenca = self.__prepocessamento_tokens(sentenca)
        versoes_sentenca = []
        for s in sentenca:
            if 'ss' in s:
                versoes_sentenca.append(self.__substituir_palavra(sentenca, s,s.replace('ss','s')))
        return versoes_sentenca

    # Ex: acesso, acessório, acessível => aceço, aceçorio, aceçivel
    def trocar_SS_to_Cdilha(self, sentenca):
        sentenca = self.__prepocessamento_tokens(sentenca)
        versoes_sentenca = []
        for s in sentenca:
            if 'ss' in s:
                versoes_sentenca.append(self.__substituir_palavra(sentenca, s,s.replace('ss','ç')))
        return versoes_sentenca

    # Ex: açafrão, almaço, dança, contorção =>  assafrão, almasso, danssa, contorssão
    def trocar_Cdilha_to_SS(self, sentenca):
        sentenca = self.__prepocessamento_tokens(sentenca)
        versoes_sentenca = []
        for s in sentenca:
            if 'ç' in s:
                versoes_sentenca.append(self.__substituir_palavra(sentenca, s,s.replace('ç','ss')))
        return versoes_sentenca

    # Ex:ansiar, cansar, descanso, hortênsia => anciar, cançar, descanço, hortência
    def trocar_S_to_C(self, sentenca):
        sentenca = self.__prepocessamento_tokens(sentenca)
        versoes_sentenca = []
        for s in sentenca:
            if 's' in s and not s.startswith('s'):
                substituicao = self.__trocar_s_to_c_cedilha(s)
                versoes_sentenca.append(self.__substituir_palavra(sentenca, s, substituicao))
        return versoes_sentenca

    def trocar_SCSCedilha_to_CCedilha(self,sentenca):
        sentenca = self.__prepocessamento_tokens(sentenca)
        versoes_sentenca = []
        for s in sentenca:
            if 'sc' in s or 'sç' in s:
                versoes_sentenca.append(self.__substituir_palavra(sentenca, s, s.replace('sc', 'c').replace('sç','c')))
        return versoes_sentenca