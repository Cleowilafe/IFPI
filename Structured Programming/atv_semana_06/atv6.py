#Entrada de dados
valor = input()

#Processamento de dados

def num(valor):
    valor = valor.strip()
    valornovo = len(valor)
    return valornovo

def main():
    valornovo = num(valor)
    print(valornovo)

#Saída de dados
if __name__ == "__main__":
    main()
