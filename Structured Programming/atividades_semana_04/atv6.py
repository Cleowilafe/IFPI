#Variavel a1 recebe valor numerico
a1 = float(input('Digite um número '))
#Variavel a2 recebe valor numerico
a2 = float(input('Digite um número '))
#Variavel soma recebe a1 + a2
soma = float(a1 + a2)
#Variavel b recebe str(a1) + str(a2)
b = str(float(a1)) + str(int(a2))
#Variavel c recebe a1 * a2
c = float(a1 * a2)
#Variavel d recebe float(a1) + int(a2)
d = str(float(a1)) * int(a2)
#Variavel e recebe a1 / a2
e = float(a1 / a2)
#Variavel f recebe a1 // a2
f = float(a1 // a2)
#Variavel g recebe a1 ** a2
g = float(a1 ** a2)
#Variavel h recebe a1 % a2
h = float(a1 % a2)
#Imprime na tela um texto com variavel soma
print(f'A soma dos números: {soma}')
#Imprime na tela um texto com variavel b
print(f'A concatenação das strings: {b}')
#Imprime na tela um texto com variavel c
print(f'A multiplicação dos números: {c}')
#Imprime na tela um texto com variavel d
print(f'A multiplicação como strings: {d}')
#Imprime na tela um texto com variavel e
print(f'A divisão dos números: {e}')
#Imprime na tela um texto com variavel f
print(f'A divisão inteira dos números: {f}')
#Imprime na tela um texto com variavel g
print(f'A exponenciação: {g}')
#Imprime na tela um texto com variavel h
print(f'O módulo (resto): {h}')