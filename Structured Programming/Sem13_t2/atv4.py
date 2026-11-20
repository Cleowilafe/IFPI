def ler_reais():
    numeros = []
    while True:
        num = int(input().strip())
        if num == 0:
            break
        numeros.append(num)
    return numeros


def soma_cumulativa(lista):
    acumulada = []
    soma = 0
    for valor in lista:
        soma += valor
        acumulada.append(soma)
    return acumulada


def main():
    lista_original = ler_reais()
    resultado = soma_cumulativa(lista_original)
    print(resultado)


if __name__ == '__main__':
    main()
