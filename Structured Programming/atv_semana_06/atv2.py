#Entrada de dados

def codigo(letra):
    return ord(letra)

def main():
    letra = input("Digite uma letra: ")
    
    #Saída de dados
    print(f"O código da letra {letra} é {codigo(letra)}.")

if __name__ == "__main__":
    main()
