def inverter(numero):
    unidade = numero % 10
    numero = numero // 10

    dezena = numero % 10
    numero = numero // 10

    centena = numero % 10
    numero = numero // 10

    milhar = numero % 10

    numero_invertido = (unidade * 1000) + (dezena * 100) + (centena * 10) + milhar

    return numero_invertido


# INPUT
numero = int(input("Digite um número de 4 dígitos: "))

# PROCESSAMENTO
numero_invertido = inverter(numero)

# OUTPUT
print(f"Número invertido: {numero_invertido}")
