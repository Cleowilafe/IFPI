def verificador(x):
    return not (
        x == "A" or x == "B" or x == "C" or x == "D" or
        x == "E" or x == "F" or x == "G" or x == "H" or
        x == "I" or x == "J" or x == "K" or x == "L" or
        x == "M" or x == "N" or x == "O" or x == "P" or
        x == "Q" or x == "R" or x == "S" or x == "T" or
        x == "U" or x == "V" or x == "W" or x == "X" or
        x == "Y" or x == "Z" or
        x == "0" or x == "1" or x == "2" or x == "3" or
        x == "4" or x == "5" or x == "6" or x == "7" or
        x == "8" or x == "9"
    )


def main():
    # INPUT
    x = input("Digite um caractere: ").strip().upper()

    # PROCESSAMENTO
    resultado = verificador(x)

    # OUTPUT
    print(f"Não é uma letra nem número? {resultado}")


if __name__ == "__main__":
    main()
