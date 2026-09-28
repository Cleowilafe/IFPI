def senhor(sexo):
    if sexo == 1:
        forma = 'Ilmo Sr.'
    else:
        forma = 'Ilma Sra.'
    return forma

def main():
#Entrada de dados
    nome = input().strip()
    sexo = int(input())
#Processamento de dados
    forma = senhor(sexo)
#Saida de dados
    print(f'{forma} {nome}')
    
if __name__ == "__main__":
    main()
