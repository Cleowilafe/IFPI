def ordenar_crescente(a, b, c):
    if a > b:
        a, b = b, a

    if a > c:
        a, c = c, a

    if b > c:
        b, c = c, b

    return a, b, c


def main():
    a = int(input())
    b = int(input())
    c = int(input())

    a, b, c = ordenar_crescente(a, b, c)

    print(a)
    print(b)
    print(c)


if __name__ == "__main__":
    main()