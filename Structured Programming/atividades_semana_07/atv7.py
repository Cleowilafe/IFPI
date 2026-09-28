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
    # Entrada de dados
    numero = int(input('Digite um número inteiro: '))

    # Processamento de dados
    quantidade = contar_pares(numero)

    # Saída de dados
    print(f'A quantidade de dígitos pares é: {quantidade}')


if __name__ == "__main__":
    main()
