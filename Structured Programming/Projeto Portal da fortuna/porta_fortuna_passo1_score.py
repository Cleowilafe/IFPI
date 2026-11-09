from random import *

score = 0

print('''
Porta da Fortuna!
=========

Existe um super prêmio atrás de uma destas 3 portas!
Adivinhe qual é a porta certa para ganhar o prêmio!

 _____  _____  _____
|     ||     ||     |
| [1] || [2] || [3] |
|  o  ||  o  ||  o  |
|_____||_____||_____|
''')

for tentativa in range(3):
    print("\nEscolha uma porta (1, 2 ou 3):")
    portaEscolhida = int(input())
    portaCerta = randint(1, 3)

    print("A porta escolhida foi a", portaEscolhida)
    print("A porta certa é a", portaCerta)

    if portaEscolhida == portaCerta:
        print("Parabéns!")
        score = score + 1
    else:
        print("Que peninha!")

print("\nSua pontuação final é", score)
