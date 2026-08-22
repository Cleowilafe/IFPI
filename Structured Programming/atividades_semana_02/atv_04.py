#===================================
# Autor [clenilson willames alves feitosa]
# status [stable]
# Version [1.0]
#===================================

valor = input("Digite a quantidade de dias que o dragão está solto: ").strip()

n_ovelhas = 0.5 # número de ovelhas por dia

devoradas = float(valor) * n_ovelhas

print(f"Foram devoradas {devoradas} ovelhas")
