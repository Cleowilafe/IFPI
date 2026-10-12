def classificar_crime(r1, r2, r3, r4, r5):
    total = 0

    if r1 == "S":
        total += 1
    if r2 == "S":
        total += 1
    if r3 == "S":
        total += 1
    if r4 == "S":
        total += 1
    if r5 == "S":
        total += 1

    if total == 2:
        return "Suspeito"
    elif total == 3 or total == 4:
        return "Cúmplice"
    elif total == 5:
        return "Assassino"
    else:
        return "Inocente"

def main():
    print("Responda às perguntas com S para Sim ou N para Não.")

    r1 = input("Telefonou para a vítima? ").strip().upper()
    r2 = input("Esteve no local do crime? ").strip().upper()
    r3 = input("Mora perto da vítima? ").strip().upper()
    r4 = input("Devia para a vítima? ").strip().upper()
    r5 = input("Já trabalhou com a vítima? ").strip().upper()

    resultado = classificar_crime(r1, r2, r3, r4, r5)
    print("Classificação:", resultado)

if __name__ == "__main__":
    main()
