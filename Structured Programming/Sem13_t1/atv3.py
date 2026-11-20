def ler_reais_inverso(n):
    reais = []
    for _ in range(n):
        valor = round(float(input().strip()), 4)
        reais.insert(0, valor)
    return reais


def ler_notas(n):
    notas = []
    for _ in range(n):
        nota = round(float(input().strip()), 1)
        notas.append(nota)
    return notas


def calcular_media(notas):
    if not notas:
        return None
    return sum(notas) / len(notas)


def processar_letras(n):
    vogais_qtd = 0
    consoantes = []
    for _ in range(n):
        letra = input().strip()[0]
        if letra.lower() in 'aeiou':
            vogais_qtd += 1
        elif letra.isalpha():
            consoantes.append(letra)
    return vogais_qtd, consoantes


def main():
    n = int(input().strip())

    # a) Valores reais na ordem inversa
    reais = ler_reais_inverso(n)
    print(reais)

    # b) Notas e média
    notas = ler_notas(n)
    media = calcular_media(notas)
    print(notas)
    if media is None:
        print("SEM NOTAS")
    else:
        print(f"{media:.1f}")

    # c) Letras, quantidade de vogais e lista de consoantes
    vogais_qtd, consoantes = processar_letras(n)
    print(vogais_qtd)
    print(consoantes)


if __name__ == '__main__':
    main()
