def avaliacao(nota1, nota2, nota3):
    med = (nota1 + nota2 + nota3) / 3

    if nota3 > 8:
        med += 1

    if med > 10:
        med = 10

    return med


def main():
    # Entrada de dados
    nota1 = float(input('Digite a primeira nota: '))
    nota2 = float(input('Digite a segunda nota: '))
    nota3 = float(input('Digite a terceira nota: '))

    # Processamento de dados
    med = avaliacao(nota1, nota2, nota3)

    # Saída de dados
    print(f'A média final é: {med:.2f}')


if __name__ == "__main__":
    main()
