def ler_numeros():
    numeros = []
    while True:
        num = int(input().strip())
        if num == 0:
            break
        numeros.append(num)
    return numeros


def multiplica_constante(lista, constante):
    nova_lista = []
    for item in lista:
        nova_lista.append(item * constante)
    return nova_lista


def main():
    lista_original = ler_numeros()
    constante = int(input().strip())
    resultado = multiplica_constante(lista_original, constante)
    print(resultado)


if __name__ == '__main__':
    main()
