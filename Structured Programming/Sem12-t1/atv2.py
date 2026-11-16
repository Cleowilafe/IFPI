def calcular_meses_compra(preco_carro):
    poupanca = 10000.0
    meses = 0

    while poupanca < preco_carro:
        poupanca *= 1.007
        preco_carro *= 1.004
        meses += 1

    return meses


def main():
    preco_inicial = float(input().strip())
    meses = calcular_meses_compra(preco_inicial)
    print(meses)


if __name__ == '__main__':
    main()
