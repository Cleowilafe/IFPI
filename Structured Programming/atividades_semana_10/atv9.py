def cantar(inicio, passo):
    for bugs in range(inicio, 0, -passo):
        print(f"{bugs} bugs no software, pegue onze deles e conserte...")
        print('Tecle "Ctrl+F5"')
    print("Sem erros no software! Está estabilizado!")

def main():
    cantar(99, 11)

if __name__ == "__main__":
    main()
