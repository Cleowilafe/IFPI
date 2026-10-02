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
    dia1 = int(input())
    mes1 = int(input())
    ano1 = int(input())

    dia2 = int(input())
    mes2 = int(input())
    ano2 = int(input())

    dia, mes, ano = data_mais_recente(
        dia1, mes1, ano1,
        dia2, mes2, ano2
    )

    print(f"{dia}/{mes}/{ano}")


if __name__ == "__main__":
    main()