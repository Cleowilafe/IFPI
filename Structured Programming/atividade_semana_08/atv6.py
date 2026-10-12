def dia_semana(numero):
    if numero == 1:
        return "domingo"
    elif numero == 2:
        return "segunda-feira"
    elif numero == 3:
        return "terça-feira"
    elif numero == 4:
        return "quarta-feira"
    elif numero == 5:
        return "quinta-feira"
    elif numero == 6:
        return "sexta-feira"
    elif numero == 7:
        return "sábado"
    else:
        return "valor inválido"

def main():
    numero = int(input("Digite um número de 1 a 7 para o dia da semana: "))
    resultado = dia_semana(numero)
    print("Dia da semana:", resultado)

if __name__ == "__main__":
    main()
