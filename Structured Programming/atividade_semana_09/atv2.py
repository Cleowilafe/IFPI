def calcular(n1, n2, operacao):
    if operacao == 1:
        return n1 + n2
    elif operacao == 2:
        return n1 - n2
    elif operacao == 3:
        return n1 * n2
    elif operacao == 4:
        return n1 / n2

def main():
    n1 = float(input("Digite o primeiro valor: "))
    n2 = float(input("Digite o segundo valor: "))
    operacao = int(input("Digite a operação (1-Adição, 2-Subtração, 3-Multiplicação, 4-Divisão): "))

    resultado = calcular(n1, n2, operacao)
    print("Resultado:", resultado)

if __name__ == "__main__":
    main()
