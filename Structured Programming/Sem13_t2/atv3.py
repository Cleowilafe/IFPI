def ler_notas(qtd):
    notas = []
    for _ in range(qtd):
        notas.append(float(input().strip()))
    return notas


def indices_aprovados(notas):
    aprovados = []
    for i, nota in enumerate(notas):
        if nota >= 6:
            aprovados.append(i)
    return aprovados


def main():
    notas = ler_notas(50)
    resultado = indices_aprovados(notas)
    print(resultado)


if __name__ == '__main__':
    main()
