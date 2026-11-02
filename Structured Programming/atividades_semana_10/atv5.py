def encontrar_maior(quantidade):
    maior = int(input("Digite o 1º número inteiro positivo: "))

    for i in range(2, quantidade + 1):
        numero = int(input(f"Digite o {i}º número inteiro positivo: "))
        if numero > maior:
            maior = numero

    return maior

def main():
    maior = encontrar_maior(100)
    print("O maior número é:", maior)

if __name__ == "__main__":
    main()
