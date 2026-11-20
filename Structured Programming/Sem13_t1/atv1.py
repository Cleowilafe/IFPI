def ler_numeros(quantidade):
    numeros = []
    for _ in range(quantidade):
        num = int(input().strip())
        numeros.append(num)
    return numeros


def calcular_soma(lista):
    soma = 0
    for num in lista:
        soma += num
    return soma


def calcular_multiplicacao(lista):
    multiplicacao = 1
    for num in lista:
        multiplicacao *= num
    return multiplicacao


def main():
    numeros = ler_numeros(10)
    soma = calcular_soma(numeros)
    multiplicacao = calcular_multiplicacao(numeros)

    print(numeros)
    print(soma)
    print(multiplicacao)


if __name__ == '__main__':
    main()
