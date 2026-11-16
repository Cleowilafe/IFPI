def calcular_fatorial(n):
    fatorial = 1
    for i in range(2, n + 1):
        fatorial *= i
    return fatorial


def main():
    numero = int(input().strip())
    resultado = calcular_fatorial(numero)
    print(resultado)


if __name__ == '__main__':
    main()
