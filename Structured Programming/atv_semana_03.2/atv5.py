tempo = int(input("Digite o tempo de serviço em anos: "))
bonus = float(input("Digite o valor do bônus por ano: "))

total = tempo * bonus

print(f"\nBonificação total: R$ {total:.2f}")