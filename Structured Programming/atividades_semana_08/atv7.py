def somar_digitos(numero):
    soma = 0

    soma += numero % 10
    numero //= 10

    soma += numero % 10
    numero //= 10

    soma += numero % 10
    numero //= 10

    soma += numero % 10
    numero //= 10

    soma += numero % 10
    numero //= 10

    soma += numero % 10

    return soma


def main():
    numero = int(input())

    if numero >= 0 and numero <= 100000:
        resultado = somar_digitos(numero)
    else:
        resultado = -1

    print(resultado)


if __name__ == "__main__":
    main()