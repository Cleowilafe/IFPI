#Entrada de dados
temperatura = float(input("Digite a temperatura em Celsius: "))

#Processamento de dados

def fahrenheit(temperatura):
    resultado = (temperatura * (9 / 5)) + 32
    return resultado

def main():
    resultado = fahrenheit(temperatura)
    
    #Saída de dados
    print(f"A temperatura em Fahrenheit é: {resultado:.2f}")

if __name__ == "__main__":
    main()
