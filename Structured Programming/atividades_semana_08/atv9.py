def calcular_peso_ideal(altura, sexo):
    if sexo == 1:
        return (72.7 * altura) - 58

    if sexo == 2:
        return (62.1 * altura) - 44.7


def main():
    altura = float(input())
    sexo = int(input())

    peso_ideal = calcular_peso_ideal(altura, sexo)

    print(f"{peso_ideal:.2f}")


if __name__ == "__main__":
    main()