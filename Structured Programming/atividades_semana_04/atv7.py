#Variavel ano recebe um valor numerico * 365
ano = 365*int(input('Digite seus anos completos '))
#Variavel mes recebe um valor numerico * 30 
mes = 30*int(input('Digite mêses que você completou esse ano '))
#Variavel dia recebe um valor numerico 
dia = int(input('Digite dias que você completou esse ano'))
#Imprime na tela um texto com a soma dos variaveis ano, mes, dia
print(f'Sua idade em dias é {ano+mes+dia}')