from random import *

jogando = True
pontuacao = 0

print('''
Vinte e um!
==========
Tente fazer exatamente 21 pontos!
''')

while jogando == True:
    numero = randint(1, 10)
    pontuacao = pontuacao + numero

    print("Seu próximo número é", numero)
    print("Sua pontuação agora é", pontuacao)

    if pontuacao > 21:
        jogando = False
    else:
        print("\nGostaria de somar mais um número? (s/n)")
        resposta = input().strip().lower()
        if resposta == 'n' or resposta == 'nao':
            jogando = False

print("\nSua pontuação final é", pontuacao)
if pontuacao == 21:
    print("VOCÊ VENCEU!!")
else:
    print("Que pena!")
