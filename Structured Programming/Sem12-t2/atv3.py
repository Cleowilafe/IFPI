def calcular_h(n):
    h = 0.0
    for i in range(1, n + 1):
        h += 1 / i
    return h


def main():
    n = int(input().strip())
    resultado = calcular_h(n)
    print(f'{resultado:.4f}')


if __name__ == '__main__':
    main()
