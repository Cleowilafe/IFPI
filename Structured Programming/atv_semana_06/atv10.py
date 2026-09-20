#Entrada de dados
temperatura = float(input())

#Processamento de dados

def fahrenheit(temperatura):
    resultado = (temperatura * (9 / 5)) + 32
    return resultado

def main():
    resultado = fahrenheit(temperatura)
    print(f"{resultado:.2f}")

#Saída de dados
if __name__ == "__main__":
    main()
