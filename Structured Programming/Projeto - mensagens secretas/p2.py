def processar_mensagem(mensagem, chave):
    alfabeto = "abcdefghijklmnopqrstuvwxyz"
    mensagem_criptografada = ""

    for char in mensagem.lower():
        if char in alfabeto:
            posicao = alfabeto.find(char)
            nova_posicao = (posicao + chave) % 26
            mensagem_criptografada += alfabeto[nova_posicao]
        else:
            mensagem_criptografada += char

    return mensagem_criptografada


def main():
    mensagem = input("Por favor, entre com a mensagem a ser criptografada: ").strip()
    chave = int(input("Por favor, entre a chave: ").strip())

    resultado = processar_mensagem(mensagem, chave)
    print("Sua mensagem criptografada é:", resultado)


if __name__ == '__main__':
    main()
