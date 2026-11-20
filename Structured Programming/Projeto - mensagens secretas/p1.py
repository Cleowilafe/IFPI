def criptografar_letra(letra, chave):
    alfabeto = "abcdefghijklmnopqrstuvwxyz"
    posicao = alfabeto.find(letra.lower())
    nova_posicao = (posicao + chave) % 26
    return alfabeto[nova_posicao]


def main():
    letra = input("Por favor, entre com uma letra para criptografar: ").strip()
    chave = int(input("Por favor, entre com a chave secreta: ").strip())

    resultado = criptografar_letra(letra, chave)
    print("Sua letra criptografada é", resultado)


if __name__ == '__main__':
    main()
