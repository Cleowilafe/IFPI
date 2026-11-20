def ler_lista(quantidade):
    lista = []
    for _ in range(quantidade):
        lista.append(int(input().strip()))
    return lista


def intercalar_listas(lista_a, lista_b):
    lista_c = []
    for i in range(len(lista_a)):
        lista_c.append(lista_a[i])
        lista_c.append(lista_b[i])
    return lista_c


def main():
    lista_a = ler_lista(25)
    lista_b = ler_lista(25)
    lista_c = intercalar_listas(lista_a, lista_b)

    print(lista_a)
    print(lista_b)
    print(lista_c)


if __name__ == '__main__':
    main()
