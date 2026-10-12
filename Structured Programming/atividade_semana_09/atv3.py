def calcular_figura(base, altura):
    if base == altura:
        return "QUADRADO"
    else:
        perimetro = 2 * (base + altura)
        area = base * altura
        return f"{perimetro} - {area}"

def main():
    base = int(input("Digite a base do retângulo: "))
    altura = int(input("Digite a altura do retângulo: "))

    resultado = calcular_figura(base, altura)
    print("Resultado:", resultado)

if __name__ == "__main__":
    main()
