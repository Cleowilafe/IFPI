def senhor(sexo):
    if sexo == 1:
        forma = 'Ilmo Sr.'
    else:
        forma = 'Ilma Sra.'
    
    return forma


def main():
    # Entrada de dados
    nome = input('Digite o nome: ').strip()
    sexo = int(input('Digite o sexo (1 - Masculino / 2 - Feminino): '))

    # Processamento de dados
    forma = senhor(sexo)

    # Saída de dados
    print(f'{forma} {nome}')


if __name__ == "__main__":
    main()
