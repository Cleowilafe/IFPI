import math

#Entrada de dados
idade = float(input("Digite sua idade em anos terrestres: "))

#Processamento de dados

def idadeespacial(idade):
    anos = idade * 0.5
    anos = math.floor(anos)
    return anos

def main():
    anos = idadeespacial(idade)
    
    #Saída de dados
    print(f"Sua idade em anos espaciais é: {anos}")

if __name__ == "__main__":
    main()
