def quantidade_caracteres(nome, estado_civil):
    if estado_civil == 1:
        conjuge = input('Digite o nome do cônjuge: ').strip()
        return len(nome) + len(conjuge)
    elif estado_civil == 2:
        return len(nome)


def main():
    # Entrada de dados
    nome = input('Digite o nome: ').strip()
    estado_civil = int(input('Digite o estado civil (1 - Casado / 2 - Solteiro): '))

    # Processamento de dados
    quantidade = quantidade_caracteres(nome, estado_civil)

    # Saída de dados
    print(f'Quantidade total de caracteres: {quantidade}')


if __name__ == "__main__":
    main()
