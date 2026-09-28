def ordenar_crescente(a, b, c):
    if a > b:
        a, b = b, a

    if a > c:
        a, c = c, a

    if b > c:
        b, c = c, b

    return a, b, c


def main():
    # Entrada de dados
    a = int(input('Digite o primeiro número: '))
    b = int(input('Digite o segundo número: '))
    c = int(input('Digite o terceiro número: '))

    # Processamento de dados
    a, b, c = ordenar_crescente(a, b, c)

    # Saída de dados
    print(f'Números em ordem crescente: {a}, {b}, {c}')


if __name__ == "__main__":
