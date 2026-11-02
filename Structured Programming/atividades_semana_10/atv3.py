def calcular_media(quantidade):
    soma = 0

    for i in range(1, quantidade + 1):
        numero = int(input(f"Digite o {i}º número inteiro: "))
        soma += numero

    return soma / quantidade

def main():
    media = calcular_media(100)
    print(f"Valor médio: {media:.2f}")

if __name__ == "__main__":
    main()
