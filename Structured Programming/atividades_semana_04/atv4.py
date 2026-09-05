#Inserir variavel h
h = int(input('Há quantas horas agora? '))
#Inserir variavel m
m = int(input('Há quantos minutos agora? '))
#Inserir variavel s
s = int(input('Há quantos segundos agora? '))
#Imprimir na tela quantos segundos se passaram desde a meia-noite
print(f'Desde a meia-noite se passaram {h*3600+m*60+s} segundos')