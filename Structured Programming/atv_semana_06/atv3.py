#Entrada de dados
segundos = int(input("Digite a quantidade de segundos: "))

#Processamento de dados

def tempo(segundos):
    hora = segundos // 3600
    min = segundos % 3600 // 60
    seg = segundos % 3600 % 60
    return hora, min, seg

def main():
    hora, min, seg = tempo(segundos)
    
    #Saída de dados
    print(f"{hora}:{min}:{seg}")

if __name__ == "__main__":
    main()
