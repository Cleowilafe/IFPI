def quantidade_caracteres(nome, estado_civil):
    if estado_civil == 1:
        conjuge = input().strip()
        return len(nome) + len(conjuge)
    elif estado_civil == 2:
        return len(nome)


def main():
    nome = input().strip()
    estado_civil = int(input())

    print(quantidade_caracteres(nome, estado_civil))


if __name__ == "__main__":
    main()