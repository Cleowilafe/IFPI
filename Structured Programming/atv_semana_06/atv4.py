
#Entrada de dados
num1 = int(input())
num2 = int(input())
num3 = int(input())
num4 = int(input())
num5 = int(input())

#Processamento de dados

def orgg(num1, num2, num3, num4, num5):
    med = (num1+ num2+ num3+ num4+ num5)/5
    maxi = max(num1, num2, num3, num4, num5)
    minn = min(num1, num2, num3, num4, num5)

    return med , maxi , minn

def main():
    med, maxi, minn = orgg(num1, num2, num3, num4, num5)
    print(maxi)
    print(minn)
    print(med)

#Saída de dados
if __name__ == "__main__":
    main()