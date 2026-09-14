def verificador(x):
    return x == "A" or x == "E" or x == "I" or x == "O" or x == "U"


def main():
    # INPUT
    x = input("Digite um caractere: ").strip().upper()

    # PROCESSAMENTO
    resultado = verificador(x)

    # OUTPUT
    print(f"É uma vogal? {resultado}")


if __name__ == "__main__":
    main()
