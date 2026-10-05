def calcular_imc(massa, altura):
    return massa / (altura ** 2)


def classificar_imc(imc):
    if imc < 18.5:
        return "Abaixo do peso"

    if imc < 25:
        return "Peso normal"

    if imc < 30:
        return "Sobrepeso"

    if imc < 35:
        return "Obeso leve"

    if imc < 40:
        return "Obeso moderado"

    return "Obeso mórbido"


def main():
    massa = float(input("Digite a massa (kg): "))
    altura = float(input("Digite a altura (m): "))

    imc = calcular_imc(massa, altura)
    classificacao = classificar_imc(imc)

    print(f"IMC: {imc:.2f}")
    print(f"Classificação: {classificacao}")


if __name__ == "__main__":
    main()
