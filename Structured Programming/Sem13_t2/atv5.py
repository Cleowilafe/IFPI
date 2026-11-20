def converter_valor(texto):
    try:
        return float(texto)
    except ValueError:
        return texto


def ler_valores(n):
    valores = []
    for _ in range(n):
        dado = input().strip()
        valores.append(converter_valor(dado))
    return valores


def esta_ordenado(lista):
    for i in range(len(lista) - 1):
        if lista[i] > lista[i + 1]:
            return False
    return True


def main():
    n = int(input().strip())
    lista = ler_valores(n)
    if esta_ordenado(lista):
        print("LISTA ORDENADA")
    else:
        print("LISTA NÃO ORDENADA")


if __name__ == '__main__':
    main()
