precos = {
    'H': 5.50,
    'C': 6.80,
    'M': 4.50,
    'A': 7.00,
    'Q': 4.00
}

total = 0.0

while True:
    print("CÓDIGO  PRODUTO         PREÇO (R$)")
    print("H       Hamburger       5,50")
    print("C       Cheeseburger    6,80")
    print("M       Misto Quente    4,50")
    print("A       Americano       7,00")
    print("Q       Queijo Prato    4,00")
    print("X       PARA TOTAL DA CONTA")

    codigo = input().strip().upper()[0]

    if codigo == 'X':
        break

    if codigo in precos:
        total += precos[codigo]
    else:
        print("Opção inválida.")

print(f"{total:.2f}")