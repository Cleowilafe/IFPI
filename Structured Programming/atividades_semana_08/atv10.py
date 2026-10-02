def calcular_media_final(nota1, nota2, nota3, media_exercicios):
    return (nota1 + 2 * nota2 + 3 * nota3 + media_exercicios) / 7


def calcular_conceito(media_final):
    if media_final >= 9.0:
        return "A"

    if media_final >= 7.5:
        return "B"

    if media_final >= 6.0:
        return "C"

    if media_final >= 4.0:
        return "D"

    return "E"


def verificar_situacao(conceito):
    if conceito == "A" or conceito == "B" or conceito == "C":
        return "Aprovado"

    return "Reprovado"


def main():
    matricula = input()

    nota1 = float(input())
    nota2 = float(input())
    nota3 = float(input())
    media_exercicios = float(input())

    media_final = calcular_media_final(
        nota1, nota2, nota3, media_exercicios
    )

    conceito = calcular_conceito(media_final)
    situacao = verificar_situacao(conceito)

    print(matricula)
    print(f"{media_final:.2f}")
    print(conceito)
    print(situacao)


if __name__ == "__main__":
    main()