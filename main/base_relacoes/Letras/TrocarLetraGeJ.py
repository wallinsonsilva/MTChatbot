import spacy
class TrocarLetraGeJ:

    def __init__(self):
        self.__vogais = ['a', 'á', 'à', 'â', 'ã', 'e', 'é', 'ê', 'i', 'í', 'î', 'o', 'ó', 'ô', 'õ', 'u', 'ú', 'û']
        self.__nlp = spacy.load('pt_core_news_md')


    def __prepocessamento_tokens(self,sentenca):
        aux = sentenca.lower();
        doc = self.__nlp(aux)
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

    def trocar_G_to_J(self, sentenca):

        sentenca = self.__prepocessamento_tokens(sentenca)
        versoes_sentenca = []

        for s in sentenca:
            if 'g' in s and not s.startswith('g'):
                posicao = s.find('g')
                if posicao != -1:
                    if s[posicao + 1] != 'u':
                        versoes_sentenca.append(self.__substituir_letra(sentenca, s, 'g', 'j'))

        return versoes_sentenca


    def trocar_J_to_G(self, sentenca):

        sentenca = self.__prepocessamento_tokens(sentenca)
        versoes_sentenca = []

        for s in sentenca:
            if 'j' in s and not s.startswith('j'):
                posicao = s.find('j')
                if posicao != -1:
                    versoes_sentenca.append(self.__substituir_letra(sentenca, s, 'j', 'g'))

        return versoes_sentenca