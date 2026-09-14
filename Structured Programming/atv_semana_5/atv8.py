def verificador(x):
    return (
        x != "A" and
        x != "E" and
        x != "I" and
        x != "O" and
        x != "U"
    )


def main():
    # INPUT
    x = input("Digite um caractere: ").strip().upper()

    # PROCESSAMENTO
    resultado = verificador(x)

    # OUTPUT
    print(f"Não é uma vogal? {resultado}")


if __name__ == "__main__":
    main()
