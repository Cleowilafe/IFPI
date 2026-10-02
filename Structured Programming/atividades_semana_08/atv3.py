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
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())

    maior, menor = maior_menor(a, b, c, d, e)

    print(maior)
    print(menor)


if __name__ == "__main__":
    main()