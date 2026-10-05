def calcular_peso_ideal(altura, sexo):
    if sexo == 1:
        return (72.7 * altura) - 58

    if sexo == 2:
        return (62.1 * altura) - 44.7


def main():
    altura = float(input("Digite a altura (m): "))
    sexo = int(input("Digite o sexo (1 - masculino, 2 - feminino): "))

    peso_ideal = calcular_peso_ideal(altura, sexo)

    print(f"Peso ideal: {peso_ideal:.2f} kg")


if __name__ == "__main__":
    main()
