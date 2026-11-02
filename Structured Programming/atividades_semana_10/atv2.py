def contar_pares_impares(quantidade):
    pares = 0
    impares = 0

    for i in range(1, quantidade + 1):
        numero = int(input(f"Digite o {i}º número inteiro positivo: "))

        if numero % 2 == 0:
            pares += 1
        else:
            impares += 1

    return pares, impares

def main():
    pares, impares = contar_pares_impares(100)
    print("Quantidade de números pares:", pares)
    print("Quantidade de números ímpares:", impares)

if __name__ == "__main__":
    main()
