distancia = int(input("Digite a distância: "))
velocidade = int(input("Digite a velocidade: "))

tempo = distancia / velocidade

dias = tempo // 24
horas = tempo % 24

print(f"\nTempo de viagem: {int(dias)} dias e {int(horas)} horas")