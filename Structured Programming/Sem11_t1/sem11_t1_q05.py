salario = float(input())
divida = float(input())

mes = 10
ano = 2016

while divida <= salario:
    mes += 1
    if mes > 12:
        mes = 1
        ano += 1
    if mes == 3:
        salario = salario * 1.05
    divida = divida * 1.15

print(f"{mes}/{ano}")
