def impar(num):
    if num % 2 != 0:
        return True
    else:
        return False


def main():
    # Entrada de dados
    num = int(input('Digite um número inteiro: '))

    # Saída de dados
    print(f'O número é ímpar? {impar(num)}')


if __name__ == "__main__":
    main()
