def impar(num):
    if num % 2 != 0:
        return True
    else:
        return False

def main():
#Entrada de dados
    num = int(input())
#Saida de dados
    print(impar(num))
    
if __name__ == "__main__":
    main()