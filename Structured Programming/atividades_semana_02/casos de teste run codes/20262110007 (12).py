#===================================
# Autor [clenilson willames alves feitosa]
# status [stable]
# Version [1.0]
#===================================

# Lendo o valor total encontrado no poço
valor_total = float(input())

# Calculando a quantidade máxima de moedas de R$0,25 usando divisão inteira
quantidade_moedas = int(valor_total // 0.25)

# Exibindo a quantidade de moedas
print(quantidade_moedas)