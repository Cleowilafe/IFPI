def mostrar_parcelas(valor, maximo):
    for parcelas in range(1, maximo + 1):
        prestacao = valor / parcelas
        print(f"{parcelas}x de R$ {prestacao:.2f}")

def main():
    valor = float(input("Digite o valor da compra (R$): "))
    mostrar_parcelas(valor, 24)

if __name__ == "__main__":
    main()
