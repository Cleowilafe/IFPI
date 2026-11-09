deposito = float(input())
taxa = float(input())

valor = deposito
anos = 0

while valor < deposito * 2:
    valor = valor * (1 + taxa / 100)
    anos += 1

print(anos)
