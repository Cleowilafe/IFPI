#Entrada de dados
valor1 = float(input("Digite o primeiro valor: "))
valor2 = float(input("Digite o segundo valor: "))

#Processamento de dados

def num(valor1, valor2):
    total = valor1 * 3 + valor2 * 2
    return total

def main():
    total = num(valor1, valor2)
    
    #Saída de dados
    print(f"O resultado é: {total:.2f}")

if __name__ == "__main__":
    main()
