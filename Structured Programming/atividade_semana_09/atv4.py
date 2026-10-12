def menor_diferenca(n1, n2, n3):
    diferenca2 = abs(n1 - n2)
    diferenca3 = abs(n1 - n3)

    if diferenca2 < diferenca3:
        return diferenca2
    else:
        return diferenca3

def main():
    n1 = int(input("Digite o primeiro número inteiro: "))
    n2 = int(input("Digite o segundo número inteiro: "))
    n3 = int(input("Digite o terceiro número inteiro: "))

    resultado = menor_diferenca(n1, n2, n3)
    print("Menor diferença:", resultado)

if __name__ == "__main__":
    main()
