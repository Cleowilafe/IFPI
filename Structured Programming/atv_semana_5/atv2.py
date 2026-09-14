def area_quadrado(lado):
    return lado * lado


def perimetro_quadrado(lado):
    return lado * 4


def main():
    # INPUT
    valor_lado = float(input("Digite o valor do lado: "))

    # PROCESSAMENTO
    area = area_quadrado(valor_lado)
    perimetro = perimetro_quadrado(valor_lado)

    # OUTPUT
    print(f"Área do quadrado: {area:10.4f}")
    print(f"Perímetro do quadrado: {perimetro:10.4f}")


if __name__ == "__main__":
    main()
