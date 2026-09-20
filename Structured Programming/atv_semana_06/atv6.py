#Entrada de dados
valor = input("Digite uma frase: ")

#Processamento de dados

def num(valor):
    valor = valor.strip()
    valornovo = len(valor)
    return valornovo

def main():
    valornovo = num(valor)
    print(f"A frase possui {valornovo} caracteres.")

#Saída de dados
if __name__ == "__main__":
    main()
