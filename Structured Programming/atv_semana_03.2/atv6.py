minutos = int(input("Digite a quantidade de minutos: "))

horas = minutos // 60
minutos_restantes = minutos % 60

print(f"\nTempo equivalente: {horas}h{minutos_restantes}min")