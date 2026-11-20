def main():
    n = int(input().strip())

    # a) Preenchida com zeros
    lista_a = [0] * n
    print(lista_a)

    # b) Preenchida de 1 a n
    lista_b = list(range(1, n + 1))
    print(lista_b)

    # c) Preenchida com n inteiros lidos do teclado
    lista_c = []
    for _ in range(n):
        valor = int(input().strip())
        lista_c.append(valor)
    print(lista_c)

    # d) Preenchida na ordem inversa usando insert
    lista_d = []
    for _ in range(n):
        valor = int(input().strip())
        lista_d.insert(0, valor)
    print(lista_d)


if __name__ == '__main__':
    main()
