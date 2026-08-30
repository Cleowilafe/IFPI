fatias = int(input("Digite a quantidade de fatias: "))
amigos = int(input("Digite a quantidade de amigos: "))

fatias_por_amigo = fatias // amigos
sobram = fatias % amigos

print(f"\nCada amigo receberá {fatias_por_amigo} fatias.")
print(f"Fatias que sobram: {sobram}")
