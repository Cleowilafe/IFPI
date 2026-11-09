quantidade = 0
soma = 0

idade = int(input())
menor = idade
maior = idade

while idade != 0:
    quantidade += 1
    soma += idade
    if idade < menor:
        menor = idade
    if idade > maior:
        maior = idade
    idade = int(input())

print(quantidade)
print(f"{soma / quantidade:.2f}")
print(menor)
print(maior)