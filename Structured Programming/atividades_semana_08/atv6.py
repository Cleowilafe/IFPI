def calcular_resultado(numero):
    if numero % 2 == 0:
        return numero + 5

    return numero + 8


def main():
    numero = int(input())

    resultado = calcular_resultado(numero)

    print(resultado)


if __name__ == "__main__":
    main()