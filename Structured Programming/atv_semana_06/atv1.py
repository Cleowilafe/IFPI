#Entrada de dados
nome = input("Escreva um nome: ")

#Processamento de dados

def ler(nome):
    nome = len(nome)
    return nome

nome = ler(nome)

#Saída de dados
def main():
    print(f"O nome possui {nome} caracteres.")

if __name__ == "__main__":
    main()
