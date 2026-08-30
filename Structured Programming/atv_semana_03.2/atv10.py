dividendo = float(input("Digite o valor do dividendo: "))
divisor = float(input("Digite o valor do divisor: "))

quociente = dividendo // divisor
resto = dividendo % divisor

print(f"\nQuociente: {quociente:.4f}")
print(f"Resto: {resto:.4f}")
