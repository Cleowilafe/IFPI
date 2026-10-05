def calcular_media(a, b, c, d, e):
    return (a + b + c + d + e) / 5


def mostrar_maiores(a, b, c, d, e, media):
    if a > media:
        print(a)

    if b > media:
        print(b)

    if c > media:
        print(c)

    if d > media:
        print(d)

    if e > media:
        print(e)


def main():
    a = int(input("Digite o primeiro número: "))
    b = int(input("Digite o segundo número: "))
    c = int(input("Digite o terceiro número: "))
    d = int(input("Digite o quarto número: "))
    e = int(input("Digite o quinto número: "))

    media = calcular_media(a, b, c, d, e)

    print(f"A média é: {media:.2f}")
    print("Números maiores que a média:")

    mostrar_maiores(a, b, c, d, e, media)


if __name__ == "__main__":
    main()
