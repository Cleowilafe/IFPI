def calcular(a, b, c):
    return 2 * a + 5 * b - c


def resultado():
    # INPUT
    a = int(input("Digite o valor de A: "))
    b = int(input("Digite o valor de B: "))
    c = int(input("Digite o valor de C: "))

    # PROCESSAMENTO
    valor = calcular(a, b, c)

    # OUTPUT
    print(f"Resultado da função: {valor}")


resultado()
