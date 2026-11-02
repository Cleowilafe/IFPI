def gerar_sequencia(inicio, fim, passo):
    texto = ""

    for numero in range(inicio, fim + 1, passo):
        if numero == fim:
            texto += f"{numero}."
        else:
            texto += f"{numero}, "

    return texto

def main():
    sequencia = gerar_sequencia(10, 1000, 10)
    print(sequencia)

if __name__ == "__main__":
    main()
