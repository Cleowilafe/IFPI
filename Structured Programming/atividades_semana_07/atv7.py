def contar_pares(numero):
    quantidade = 0

    if numero >= 100:
        centenas = numero // 100

        if centenas % 2 == 0:
            quantidade += 1

    dezenas = (numero // 10) % 10
    unidades = numero % 10

    if dezenas % 2 == 0:
        quantidade += 1

    if unidades % 2 == 0:
        quantidade += 1

    return quantidade


def main():
    numero = int(input())

    print(contar_pares(numero))


if __name__ == "__main__":
    main()