def escrever_numero(n):
    c = n // 100
    d = (n % 100) // 10
    u = n % 10

    if c == 1:
        centena = "uma centena"
    elif c == 2:
        centena = "duas centenas"
    elif c == 3:
        centena = "três centenas"
    elif c == 4:
        centena = "quatro centenas"
    elif c == 5:
        centena = "cinco centenas"
    elif c == 6:
        centena = "seis centenas"
    elif c == 7:
        centena = "sete centenas"
    elif c == 8:
        centena = "oito centenas"
    elif c == 9:
        centena = "nove centenas"

    if d == 1:
        dezena = "uma dezena"
    elif d == 2:
        dezena = "duas dezenas"
    elif d == 3:
        dezena = "três dezenas"
    elif d == 4:
        dezena = "quatro dezenas"
    elif d == 5:
        dezena = "cinco dezenas"
    elif d == 6:
        dezena = "seis dezenas"
    elif d == 7:
        dezena = "sete dezenas"
    elif d == 8:
        dezena = "oito dezenas"
    elif d == 9:
        dezena = "nove dezenas"

    if u == 1:
        unidade = "uma unidade"
    elif u == 2:
        unidade = "duas unidades"
    elif u == 3:
        unidade = "três unidades"
    elif u == 4:
        unidade = "quatro unidades"
    elif u == 5:
        unidade = "cinco unidades"
    elif u == 6:
        unidade = "seis unidades"
    elif u == 7:
        unidade = "sete unidades"
    elif u == 8:
        unidade = "oito unidades"
    elif u == 9:
        unidade = "nove unidades"

    if c > 0 and d > 0 and u > 0:
        return f"{centena}, {dezena} e {unidade}."
    elif c > 0 and d > 0:
        return f"{centena} e {dezena}."
    elif c > 0 and u > 0:
        return f"{centena} e {unidade}."
    elif d > 0 and u > 0:
        return f"{dezena} e {unidade}."
    elif c > 0:
        return centena + "."
    elif d > 0:
        return dezena + "."
    elif u > 0:
        return unidade + "."
    else:
        return "zero."

def main():
    n = int(input("Digite um número inteiro menor que 1000: "))
    resultado = escrever_numero(n)
    print("Por extenso:", resultado)

if __name__ == "__main__":
    main()
