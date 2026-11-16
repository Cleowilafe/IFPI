def eh_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True


def listar_primos(x, y):
    inicio = min(x, y)
    fim = max(x, y)
    primos = []
    for num in range(inicio, fim + 1):
        if eh_primo(num):
            primos.append(num)
    return primos


def main():
    x = int(input().strip())
    y = int(input().strip())
    for primo in listar_primos(x, y):
        print(primo)


if __name__ == '__main__':
    main()
