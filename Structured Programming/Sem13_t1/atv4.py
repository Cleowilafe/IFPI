def ler_numeros(quantidade):
    numeros = []
    for _ in range(quantidade):
        num = int(input().strip())
        numeros.append(num)
    return numeros


def separar_pares_impares(numeros):
    par = []
    impar = []
    for num in numeros:
        if num % 2 == 0:
            par.append(num)
        else:
            impar.append(num)
    return par, impar


def main():
    numeros = ler_numeros(20)
    par, impar = separar_pares_impares(numeros)

    print(numeros)
    print(par)
    print(impar)


if __name__ == '__main__':
    main()
