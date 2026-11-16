def calcular_numero_sorte(data_nascimento):
    soma = 0

    while data_nascimento > 0:
        soma += data_nascimento % 10
        data_nascimento //= 10

    return soma


def main():
    data = int(input().strip())
    numero_sorte = calcular_numero_sorte(data)
    print(numero_sorte)


if __name__ == '__main__':
    main()
