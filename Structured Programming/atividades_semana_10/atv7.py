def cantar(inicio, fim):
    for bugs in range(inicio, fim + 1):
        print(f"{bugs} bugs no software, pegue um deles e conserte...")
        print('Tecle "Ctrl+F5"')
    print("Vamos fazer mais um café!")

def main():
    cantar(99, 250)

if __name__ == "__main__":
    main()
