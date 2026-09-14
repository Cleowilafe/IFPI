def area_quadrado(lado):
    return lado * lado


def perimetro_quadrado(lado):
    return lado * 4


# INPUT
valor_lado = float(input("Digite o valor do lado: "))

# PROCESSAMENTO
area = area_quadrado(valor_lado)
perimetro = perimetro_quadrado(valor_lado)

# OUTPUT
print("Área do quadrado: %10.4f" % area)
print("Perímetro do quadrado: %10.4f" % perimetro)
