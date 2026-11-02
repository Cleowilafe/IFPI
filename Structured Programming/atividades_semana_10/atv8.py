def cantar(inicio, fim, passo):
    for bugs in range(inicio, fim + 1, passo):
        print(f"{bugs} bugs no software, pegue sete deles e conserte...")
        print('Tecle "Ctrl+F5"')
    print("Vamos fazer mais um café!")

def main():
    cantar(99, 250, 7)

if __name__ == "__main__":
    main()
