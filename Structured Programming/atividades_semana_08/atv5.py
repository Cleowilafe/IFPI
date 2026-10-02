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
    massa = float(input())
    altura = float(input())

    imc = calcular_imc(massa, altura)
    classificacao = classificar_imc(imc)

    print(f"{imc:.2f}")
    print(classificacao)


if __name__ == "__main__":
    main()