from main.SubstituicoesPalavras.Tradutor import Tradutor

t = Tradutor()
versoes_traducao = t.versoes_sentencas_traduzidas('Eu quero agora')
# versoes_traducao = t.versoes_sentencas_traduzidas('Eu quero mudar meu email e telefone agora')
print(versoes_traducao)

print('=============TRADUÇÕES=================')
for v in versoes_traducao:
    print(v)
print('=============TRADUÇÕES=================')

# sentencas = ['Quero mudar meu e-mail e telefone imediatamente', 'Eu quero mudar meu email e número de telefone agora']
print(t.traduzir_sentencas_en(versoes_traducao))

# print('\n')
# x = Sinonimo()

# print(x.sinonimos_elementos('i want to change my email and phone now'))
# print('=============SINONIMOS=================')
# for v in versoes_traducao:
#     print(v)
#     for s in x.versoes_sentenca(v, deep=1):
#         print('----',s)


# for s in x.versoes_sentenca('eu quero mudar meu email e telefone agora', deep=1):
#     print('----',s)

