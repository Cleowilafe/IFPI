def calcular(a, b, c):
    return 2 * a + 5 * b - c


def main():
    # INPUT
    a = int(input("Digite o valor de A: "))
    b = int(input("Digite o valor de B: "))
    c = int(input("Digite o valor de C: "))

    # PROCESSAMENTO
    resultado = calcular(a, b, c)

    # OUTPUT
    print(f"Resultado da função: {resultado}")


if __name__ == "__main__":
    main()
