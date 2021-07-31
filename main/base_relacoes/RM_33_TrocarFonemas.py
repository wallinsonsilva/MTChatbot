from main.base_relacoes.Letras.TrocarLetraX import TrocarLetraX
from main.base_relacoes.Letras.TrocarLetraGeJ import TrocarLetraGeJ
from main.base_relacoes.Letras.TrocarLetraLeU import TrocarLetraLeU
from main.base_relacoes.Letras.TrocarLetraSCCedilhaSS import TrocarLetraSCCedilhaSS

class RM_33_TrocaFonemas:

    def __init__(self):
        self.trocar_xch = TrocarLetraX()
        self.trocar_gej = TrocarLetraGeJ()
        self.trocar_leu = TrocarLetraLeU()
        self.trocar_sccedilhass = TrocarLetraSCCedilhaSS()

    # RM3.3.1, RM3.3.2, RM3.3.3, RM3.3.4
    def rm_33_1_2_3_4_trocar_x(self,sentenca):
        return self.trocar_xch.trocar_x(sentenca)

    # RM3.3.5 G -> J
    def rm_33_5_trocar_g_por_j(self,sentenca):
        return self.trocar_gej.trocar_G_to_J(sentenca)

    # RM3.3.5 J -> G
    def rm_33_5_trocar_j_por_g(self, sentenca):
        return self.trocar_gej.trocar_J_to_G(sentenca)

    # RM3.3.6 S -> Z
    def rm_33_6_trocar_s_por_z(self,sentenca):
        return self.trocar_sccedilhass.trocar_S_to_Z(sentenca)

    # RM3.3.7 SS -> S
    def rm_33_7_trocar_ss_por_s(self, sentenca):
        return self.trocar_sccedilhass.trocar_SS_to_S(sentenca)

    # RM3.3.8 SS -> Ç
    def rm_33_8_trocar_ss_por_cedilha(self, sentenca):
        return self.trocar_sccedilhass.trocar_SS_to_Cdilha(sentenca)

    # RM3.3.9 S -> C
    def rm_33_9_trocar_s_por_c(self, sentenca):
        return self.trocar_sccedilhass.trocar_S_to_C(sentenca)

    # RM3.3.10 e  RM3.3.11 SC -> C e SC -> Ç
    def rm_33_10_11_trocar_sc_por_c(self, sentenca):
        return self.trocar_sccedilhass.trocar_SCSCedilha_to_CCedilha(sentenca)

    # RM3.3.12
    def rm_33_12_trocar_l_por_u(self, sentenca):
        return self.trocar_leu.trocar_L_to_U(sentenca)