def calcular_compra(morango, maca):
    if morango <= 5:
        valor_morango = morango * 2.50
    else:
        valor_morango = morango * 2.20

    if maca <= 5:
        valor_maca = maca * 1.80
    else:
        valor_maca = maca * 1.50

    total = valor_morango + valor_maca

    if morango + maca > 8 or total > 25:
        total = total * 0.90

    return total

def main():
    morango = float(input("Digite a quantidade de morangos em Kg: "))
    maca = float(input("Digite a quantidade de maçãs em Kg: "))

    resultado = calcular_compra(morango, maca)
    print(f"Valor total a pagar: R$ {resultado:.2f}")

if __name__ == "__main__":
    main()
