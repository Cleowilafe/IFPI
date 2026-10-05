def maior_menor(a, b, c, d, e):
    maior = a
    menor = a

    if b > maior:
        maior = b
    if b < menor:
        menor = b

    if c > maior:
        maior = c
    if c < menor:
        menor = c

    if d > maior:
        maior = d
    if d < menor:
        menor = d

    if e > maior:
        maior = e
    if e < menor:
        menor = e

    return maior, menor


def main():
    a = int(input("Digite o primeiro número: "))
    b = int(input("Digite o segundo número: "))
    c = int(input("Digite o terceiro número: "))
    d = int(input("Digite o quarto número: "))
    e = int(input("Digite o quinto número: "))

    maior, menor = maior_menor(a, b, c, d, e)

    print("Maior número:", maior)
    print("Menor número:", menor)


if __name__ == "__main__":
    main()
