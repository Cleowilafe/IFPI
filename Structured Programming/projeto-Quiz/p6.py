score = 0

print('''Q1 - Em Naruto, qual é o nome da técnica usada por Naruto que cria vários clones de si mesmo?
a - Rasengan
b - Kage Bunshin no Jutsu
c - Chidori
''')

resposta = input().lower()

if resposta == 'a':
    print("Não - Rasengan é outra técnica :(")
elif resposta == 'b':
    print("Correto!! :)")
    score += 1
elif resposta == 'c':
    print("Não - essa é uma técnica associada ao Sasuke :(")
else:
    print("Você não escolheu a, b ou c :(")


print('''Q2 - Em One Piece, qual é o sonho de Monkey D. Luffy?
a - Tornar-se o Rei dos Piratas
b - Tornar-se o maior espadachim do mundo
c - Encontrar o All Blue
''')

resposta = input().lower()

if resposta == 'a':
    print("Correto!! :)")
    score += 1
elif resposta == 'b':
    print("Não - esse é o sonho do Zoro :(")
elif resposta == 'c':
    print("Não - esse é o sonho do Sanji :(")
else:
    print("Você não escolheu a, b ou c :(")


print('''Q3 - Em Attack on Titan, qual é o nome da tropa responsável por explorar o território fora das muralhas?
a - Polícia Militar
b - Tropa de Guarnição
c - Tropa de Exploração
''')

resposta = input().lower()

if resposta == 'a':
    print("Não - a Polícia Militar atua principalmente no interior das muralhas :(")
elif resposta == 'b':
    print("Não - a Guarnição é responsável pela defesa das muralhas :(")
elif resposta == 'c':
    print("Correto!! :)")
    score += 1
else:
    print("Você não escolheu a, b ou c :(")


print("Obrigado por jogar!")
print(f'Seu score é {score}')

