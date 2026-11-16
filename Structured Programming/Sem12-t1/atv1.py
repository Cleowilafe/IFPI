def calcular_tempo_alcance(vantagem_metros):
    pos_tartaruga = vantagem_metros
    pos_lebre = 0
    minutos = 0

    while pos_lebre < pos_tartaruga:
        pos_tartaruga += 1
        pos_lebre += 10
        minutos += 1

    return minutos


def main():
    vantagem = int(input().strip())
    tempo = calcular_tempo_alcance(vantagem)
    print(tempo)


if __name__ == '__main__':
    main()
