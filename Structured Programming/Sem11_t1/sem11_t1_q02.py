soma = 0
quantidade = 0

numero = int(input())
while numero != 0:
    soma += numero
    quantidade += 1
    numero = int(input())

print(f'{soma / quantidade:.2f}')
