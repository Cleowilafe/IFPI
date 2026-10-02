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
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())

    media = calcular_media(a, b, c, d, e)

    print(f"{media:.2f}")

    mostrar_maiores(a, b, c, d, e, media)


if __name__ == "__main__":
    main()