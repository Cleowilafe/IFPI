def min_para_hrs(qtd_minutos):
    horas = qtd_minutos // 60
    minutos = qtd_minutos % 60

    return f"{horas}:{minutos:02d}"


def main():
    # INPUT
    minutos = int(input("Digite a quantidade de minutos: "))

    # PROCESSAMENTO
    horas = min_para_hrs(minutos)

    # OUTPUT
    print(f"Horário convertido: {horas}")


if __name__ == "__main__":
    main()
