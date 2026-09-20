#Entrada de dados
preco = float(input("Digite o preço: "))

#Processamento de dados

def val(preco):
    desconto = preco * 0.91
    normal = preco / 5
    aumento = (preco * 1.17) / 10
    return desconto, normal, aumento

def main():
    desconto, normal, aumento = val(preco)
    
    #Saída de dados
    print(f"Preço com desconto: {desconto:.2f}")
    print(f"Preço normal parcelado: {normal:.2f}")
    print(f"Preço com aumento parcelado: {aumento:.2f}")

if __name__ == "__main__":
    main()
