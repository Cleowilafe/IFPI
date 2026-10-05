def data_mais_recente(dia1, mes1, ano1, dia2, mes2, ano2):

    if ano1 > ano2:
        return dia1, mes1, ano1

    if ano2 > ano1:
        return dia2, mes2, ano2

    if mes1 > mes2:
        return dia1, mes1, ano1

    if mes2 > mes1:
        return dia2, mes2, ano2

    if dia1 > dia2:
        return dia1, mes1, ano1

    return dia2, mes2, ano2


def main():
    dia1 = int(input("Digite o dia da primeira data: "))
    mes1 = int(input("Digite o mês da primeira data: "))
    ano1 = int(input("Digite o ano da primeira data: "))

    dia2 = int(input("Digite o dia da segunda data: "))
    mes2 = int(input("Digite o mês da segunda data: "))
    ano2 = int(input("Digite o ano da segunda data: "))

    dia, mes, ano = data_mais_recente(
        dia1, mes1, ano1,
        dia2, mes2, ano2
    )

    print(f"A data mais recente é: {dia}/{mes}/{ano}")


if __name__ == "__main__":
    main()
