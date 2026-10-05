def verificar_numero(numero):
    if numero % 3 == 0 and numero % 5 == 0:
        return "FIZZBUZZ"

    if numero % 3 == 0:
        return "FIZZ"

    if numero % 5 == 0:
        return "BUZZ"

    return numero


def main():
    numero = int(input("Digite um número inteiro: "))

    resultado = verificar_numero(numero)

    print("Resultado:", resultado)


if __name__ == "__main__":
    main()
