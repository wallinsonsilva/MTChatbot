from main.dao.relacoes_dao import RelacoesDAO
from main.dao.caso_teste_origem_dao import SourceTestCaseDAO
from main.dao.caso_teste_acompanhamento_dao import NovasSentencasDAO
from main.dao.resultado_teste_dao import ResultadoTesteDAO
from main.dao.quantidade_sentenca_gerada_dao import QuantidadeSentecaGeradaRMDAO
from main.dao.hist_confianca_acompanhamento_dao import HistConfiancaAcompanhamentoDAO
from main.model.relacao import Relacao
from main.model.caso_teste_origem import SourceTestCase
from main.model.caso_teste_acompanhamento import FollowUpTestCase
from main.model.resultado_teste import Resultado
from main.model.resultado_completo import ResultadoCompleto
from main.model.quantidade_sentenca_gerada import QuantidadeSentecaGeradaRM
from main.model.hist_confianca_acompanhamento import HistConfiancaAcompanhamento

from main.config.Banco import Banco

# rel_dao = RelacoesDAO()
# ent_dao = SourceTestCaseDAO()
# sen_dao = NovasSentencasDAO()
# res_dao = ResultadoTesteDAO()


#Base: Relações
# r1 = Relacao(nome_rm='RM1',observacao='Sem Observação')
# r2 = Relacao(nome_rm='RM2',observacao=None)
# rel_dao.add_relacao(r1)
# rel_dao.add_relacao(r2)

#Base: Source Test Case
# cto1 = SourceTestCase(entrada="Olá essa é sentenca 1.",resposta_app='Entrada Sentenca 1')
# cto2 = SourceTestCase(entrada="Olá essa é sentenca 2.",resposta_app='Entrada Sentenca 2')
# ent_dao.add_entrada(cto1)
# ent_dao.add_entrada(cto2)

#Base: Follow Up Test Case
# ftc1 = FollowUpTestCase(entrada_id=1,rm_id=5,sentenca="Olá essa é sentenca alterada 1.")
# ftc12 = FollowUpTestCase(entrada_id=1,rm_id=5,sentenca="Olá essa é sentenca alterada 12.")
# ftc13 = FollowUpTestCase(entrada_id=1,rm_id=4,sentenca="Olá essa é sentenca alterada 13.")
# ftc14 = FollowUpTestCase(entrada_id=1,rm_id=4,sentenca="Olá essa é sentenca alterada 14.")
# sen_dao.add_nova_sentenca(ftc1)
# sen_dao.add_nova_sentenca(ftc12)
# sen_dao.add_nova_sentenca(ftc13)
# sen_dao.add_nova_sentenca(ftc14)

# ftc2 = FollowUpTestCase(entrada_id=2,rm_id=5,sentenca="Olá essa é sentenca alterada 2.")
# ftc22 = FollowUpTestCase(entrada_id=2,rm_id=5,sentenca="Olá essa é sentenca alterada 22.")
# ftc23 = FollowUpTestCase(entrada_id=2,rm_id=4,sentenca="Olá essa é sentenca alterada 23.")
# ftc24 = FollowUpTestCase(entrada_id=2,rm_id=4,sentenca="Olá essa é sentenca alterada 24.")
# sen_dao.add_nova_sentenca(ftc2)
# sen_dao.add_nova_sentenca(ftc22)
# sen_dao.add_nova_sentenca(ftc23)
# sen_dao.add_nova_sentenca(ftc24)


#Base: Resultado
# r1 = Resultado(rm_id=5,sentenca_id=2,resposta_app="Entrada 1",resultado_teste="PASSOU")
# r11 = Resultado(rm_id=5,sentenca_id=2,resposta_app="Entrada 1",resultado_teste="FALHOU")
# r12 = Resultado(rm_id=5,sentenca_id=2,resposta_app="Entrada 1",resultado_teste="PASSOU")
# r2 = Resultado(rm_id=5,sentenca_id=3,resposta_app="Entrada 12",resultado_teste="FALHOU")
# r3 = Resultado(rm_id=4,sentenca_id=4,resposta_app="Entrada 13",resultado_teste="PASSOU")
# r4 = Resultado(rm_id=4,sentenca_id=5,resposta_app="Entrada 14",resultado_teste="FALHOU")
# r5 = Resultado(rm_id=5,sentenca_id=6,resposta_app="Entrada 2",resultado_teste="PASSOU")
# r6 = Resultado(rm_id=5,sentenca_id=7,resposta_app="Entrada 22",resultado_teste="PASSOU")
# r7 = Resultado(rm_id=4,sentenca_id=8,resposta_app="Entrada 23",resultado_teste="FALHOU")
# r8 = Resultado(rm_id=4,sentenca_id=9,resposta_app="Entrada 24",resultado_teste="PASSOU")
# res_dao.add_resultado(r1)
# res_dao.add_resultado(r11)
# res_dao.add_resultado(r12)
# res_dao.add_resultado(r2)
# res_dao.add_resultado(r3)
# res_dao.add_resultado(r4)
# res_dao.add_resultado(r5)
# res_dao.add_resultado(r6)
# res_dao.add_resultado(r7)
# res_dao.add_resultado(r8)

conn = Banco().getConnection()
hist_dao = HistConfiancaAcompanhamentoDAO(conn)
hist_dao.get_historico_detalhade_completo()
