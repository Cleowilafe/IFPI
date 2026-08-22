#===================================
# Autor [clenilson willames alves feitosa]
# status [stable]
# Version [1.0]
#===================================

# Lendo os volumes das duas substâncias
volume1 = float(input("Digite a quantidade em litros da primeira substância: ").strip())
volume2 = float(input("Digite a quantidade em litros da segunda substância: ").strip())

# Calculando o total da poção
total = volume1 + volume2

# Exibindo o resultado formatado
print( f"O volume total é: {total} (L)")
