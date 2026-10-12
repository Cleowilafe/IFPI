def calcular(n):
    resto = n % 5

    if resto == 0:
        return 9 * n + 7
    elif resto == 1:
        if n % 2 == 0:
            return "par"
        else:
            return "ímpar"
    elif resto == 2:
        return 5 * n**2 - 3 * n + 42
    elif resto == 3:
        return n // 10
    elif resto == 4:
        return n**2

def main():
    n = int(input("Digite um número inteiro: "))
    resultado = calcular(n)
    print("Resultado:", resultado)

if __name__ == "__main__":
    main()
