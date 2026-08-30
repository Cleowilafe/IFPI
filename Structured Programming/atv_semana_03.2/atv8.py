doces = int(input("Digite a quantidade de doces produzidos: "))
pacotes = int(input("Digite a quantidade de pacotes disponíveis: "))

doces_por_pacote = doces // pacotes

print(f"\nCada pacote terá {doces_por_pacote} doces.")