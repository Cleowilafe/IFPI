#Entrada de dados
preco = float(input())

#Processamento de dados

def val(preco):
    desconto = preco * 0.91
    normal = preco / 5
    aumento = (preco * 1.17) / 10
    return desconto, normal, aumento

def main():
    desconto, normal, aumento = val(preco)
    print(f'{desconto:.2f}')
    print(f'{normal:.2f}')
    print(f'{aumento:.2f}')

#Saída de dados
if __name__ == "__main__":
    main()
