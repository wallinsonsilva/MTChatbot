from main.Letras.TrocarCaractere import TrocarCaracteres

# RM3.2
class TrocaLetras:

    def __init__(self):
        self.tc = TrocarCaracteres()

    # RM3.2 (RM2.1.2)
    def rm_32_212_troca_caractere_proximo_teclado(self,sentenca):
        return self.tc.trocar_caracteres_vizinhos_teclado(sentenca)

    # RM3.2 (RM2.1.3)
    def rm_32_213_deletar_caractere(self,sentenca):
        return self.tc.deletar_caracteres_vizinhos_sentenca(sentenca)

    # RM3.2
    def rm_32_1_troca_caractere_proximo_palavra(self,sentenca):
        return self.tc.trocar_caracteres_vizinhos_palavra(sentenca)



