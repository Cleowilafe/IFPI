#Inserir o valor da variável a
a = int(input('Digite a altura da parede '))
#Inserir o valor da variável c
c = int(input('Digite o comprimento da parede '))
#Inserir o valor da variável l
l = int(input('Digite a largura da parede '))
#variavel area é calculado por formula c * l
area = (c * l) 
#variavel volume é calculado por formula l*c*a
volume = (l * c * a)
#variavel f é calculado por formula (2*a*l)+(2*a*c)
f = (2* a * l) + (2 * a * c)
#Imprime na tela Área do piso da sala
print(f'Área do piso da sala é igual a {area} m^2')
#Imprime na tela Volume da sala
print(f'Volume da sala é igual a {volume} m^3')
#Imprime na tela Área das paredes da sala
print(f'Área das paredes da sala é igual a {f} m^2')