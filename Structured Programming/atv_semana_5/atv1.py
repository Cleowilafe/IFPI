def percentual(valor, porcentagem):
    return valor * (porcentagem / 100)


def calcular_acrescimo(preco, porcentagem):
    return preco + percentual(preco, porcentagem)


def calcular_desconto(preco, porcentagem):
    return preco - percentual(preco, porcentagem)


# INPUT
preco = float(input())
valor_percentual = float(input())

# PROCESSAMENTO
preco_acres = calcular_acrescimo(preco, valor_percentual)
preco_desc = calcular_desconto(preco, valor_percentual)

# OUTPUT
print("%.2f" % preco_acres)
print("%.2f" % preco_desc)
