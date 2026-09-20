#Entrada de dados
valor1 = float(input())
valor2 = float(input())
#Processamento de dados

def num(valor1, valor2):
    total = valor1*3 + valor2*2
    return total

def main():
    total = num(valor1, valor2)
    print(f'{total:.2f}')

#Saída de dados
if __name__ == "__main__":
    main()