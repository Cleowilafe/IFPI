def calcular_anos_ultrapassagem(p1, p2):
    pop_a = max(p1, p2)
    pop_b = min(p1, p2)
    anos = 0

    while pop_b <= pop_a:
        pop_a *= 1.02
        pop_b *= 1.03
        anos += 1

    return anos


def main():
    p1 = float(input().strip())
    p2 = float(input().strip())
    anos = calcular_anos_ultrapassagem(p1, p2)
    print(anos)


if __name__ == '__main__':
    main()
