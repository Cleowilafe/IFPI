raio = float(input("Digite o valor do raio: "))

pi = 3.141592

comprimento = 2 * pi * raio
area_circulo = pi * raio ** 2
area_esfera = 4 * pi * raio ** 2
volume_esfera = (4 / 3) * pi * raio ** 3

print(f"\nComprimento da circunferência: {comprimento:.6f}")
print(f"Área do círculo: {area_circulo:.6f}")
print(f"Área da esfera: {area_esfera:.6f}")
print(f"Volume da esfera: {volume_esfera:.6f}")