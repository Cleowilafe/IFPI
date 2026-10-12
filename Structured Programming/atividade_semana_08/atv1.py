def verificar_numeros(n1, n2, n3):
    if n1 == n2 == n3:
        return "Todos os valores são iguais"
    elif n1 != n2 and n1 != n3 and n2 != n3:
        return "Todos os valores são diferentes"
    else:
        return "Existem dois valores iguais e um diferente"

def main():
    n1 = int(input("Digite o primeiro número inteiro: "))
    n2 = int(input("Digite o segundo número inteiro: "))
    n3 = int(input("Digite o terceiro número inteiro: "))

    resultado = verificar_numeros(n1, n2, n3)
    print("Resultado:", resultado)

if __name__ == "__main__":
    main()
