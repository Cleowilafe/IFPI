def gerar_fibonacci(n):
    termos = [0, 1]
    for _ in range(2, n):
        proximo = termos[-1] + termos[-2]
        termos.append(proximo)
    return termos


def main():
    n = int(input().strip())
    sequencia = gerar_fibonacci(n)
    print(', '.join(map(str, sequencia)))


if __name__ == '__main__':
    main()
