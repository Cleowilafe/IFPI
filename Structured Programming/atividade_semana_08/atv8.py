def data_valida(data):
    dia = data // 1000000
    mes = (data // 10000) % 100
    ano = data % 10000

    if ano < 1 or mes < 1 or mes > 12 or dia < 1:
        return False

    if mes == 2:
        if ano % 400 == 0 or (ano % 4 == 0 and ano % 100 != 0):
            return dia <= 29
        else:
            return dia <= 28

    elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
        return dia <= 30

    else:
        return dia <= 31

def main():
    data = int(input("Digite a data no formato DDMMAAAA: "))
    resultado = data_valida(data)
    print("A data é válida:", resultado)

if __name__ == "__main__":
    main()
