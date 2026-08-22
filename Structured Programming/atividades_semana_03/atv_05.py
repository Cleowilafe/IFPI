#===================================
# Autor [clenilson willames alves feitosa]
# status [stable]
# Version [1.0]
#===================================


s_marte = input("Digite a distância até marte (km): ").strip()
vel_nave = input("Digite a velocidade média da nave (km/h): ").strip()

tempo = float(s_marte) / float (vel_nave)

print (f"Você chegará em marte em {tempo} horas")


