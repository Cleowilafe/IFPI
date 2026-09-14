def verificador(x):
    return (
        x == "A" or x == "B" or x == "C" or x == "D" or
        x == "E" or x == "F" or x == "G" or x == "H" or
        x == "I" or x == "J" or x == "K" or x == "L" or
        x == "M" or x == "N" or x == "O" or x == "P" or
        x == "Q" or x == "R" or x == "S" or x == "T" or
        x == "U" or x == "V" or x == "W" or x == "X" or
        x == "Y" or x == "Z"
    )


def main():
    # INPUT
    x = input("Digite um caractere: ").strip().upper()

    # PROCESSAMENTO
    resultado = verificador(x)

    # OUTPUT
    print(f"É uma letra? {resultado}")


if __name__ == "__main__":
    main()
