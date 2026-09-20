import math

#Entrada de dados
idade = float(input())

#Processamento de dados

def idadeespacial(idade):
    anos = idade * 0.5
    anos = math.floor(anos)
    return anos

def main():
    anos = idadeespacial(idade)
    print(anos)

#Saída de dados
if __name__ == "__main__":
    main()
