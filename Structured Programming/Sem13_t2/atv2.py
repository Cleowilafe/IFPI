def ler_lista(qtd):
    numeros = []
    for _ in range(qtd):
        numeros.append(int(input().strip()))
    return numeros


def transformar_ordenados(lista):
    ordenada = sorted(lista)
    resultado = []
    for i, valor in enumerate(ordenada):
        if i % 2 == 0:
            resultado.append(valor * 3)
        else:
            resultado.append(valor * 5)
    return resultado


def main():
    numeros = ler_lista(100)
    nova_lista = transformar_ordenados(numeros)
    print(nova_lista)


if __name__ == '__main__':
    main()
