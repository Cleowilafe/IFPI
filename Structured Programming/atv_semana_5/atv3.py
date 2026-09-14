def min_para_hrs(qtd_minutos):
    horas = qtd_minutos // 60
    minutos = qtd_minutos % 60
    return f"{horas}:{minutos:02d}"


# INPUT
minutos = int(input("Digite a quantidade de minutos: "))

# PROCESSAMENTO
horas = min_para_hrs(minutos)

# OUTPUT
print(f"Horário convertido: {horas}")
