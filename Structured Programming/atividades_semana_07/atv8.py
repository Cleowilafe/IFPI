def analisar_numero(numero):
    dezenas = numero // 10
    unidades = numero % 10

    impares = 0

    if dezenas % 2 != 0:
        impares += 1

    if unidades % 2 != 0:
        impares += 1

    if impares == 0:
        return "Nenhum dígito é ímpar."
    elif impares == 1:
        return "Apenas um dígito é ímpar."
    else:
        return "Os dois dígitos são ímpares."


def main():
    # Entrada de dados
    numero = int(input('Digite um número inteiro: '))

    # Processamento de dados
    resultado = analisar_numero(numero)

    # Saída de dados
    print(f'Resultado: {resultado}')


if __name__ == "__main__":
    main()
