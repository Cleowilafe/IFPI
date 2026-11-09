numero = int(input())
maior = numero
menor = numero

while numero != 0:
    if numero > maior:
        maior = numero
    if numero < menor:
        menor = numero
    numero = int(input())

print(maior)
print(menor)
