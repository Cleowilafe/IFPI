def percentual(valor, porcentagem):
    return valor * (porcentagem / 100)


def calcular_acrescimo(preco, porcentagem):
    return preco + percentual(preco, porcentagem)


def calcular_desconto(preco, porcentagem):
    return preco - percentual(preco, porcentagem)


def main():
    # INPUT
    preco = float(input("Digite o preço: "))
    valor_percentual = float(input("Digite o percentual: "))

    # PROCESSAMENTO
    preco_acres = calcular_acrescimo(preco, valor_percentual)
    preco_desc = calcular_desconto(preco, valor_percentual)

    # OUTPUT
    print(f"Preço com acréscimo: {preco_acres:.2f}")
    print(f"Preço com desconto: {preco_desc:.2f}")


if __name__ == "__main__":
    main()
