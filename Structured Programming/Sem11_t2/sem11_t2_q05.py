nota = float(input())

while nota < 0 or nota > 10:
    print("Nota inválida.")
    nota = float(input())

if nota >= 8.5:
    print("A")
elif nota >= 7.0:
    print("B")
elif nota >= 5.0:
    print("C")
elif nota >= 4.0:
    print("D")
else:
    print("E")
