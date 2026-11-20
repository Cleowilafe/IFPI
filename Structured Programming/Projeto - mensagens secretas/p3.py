def cifra_avancada(mensagem, chave_inicial):
    alfabeto = "qwertyuiopasdfghjklzxcvbnm"
    mensagem_criptografada = ""
    chave = chave_inicial

    for char in mensagem.lower():
        if char in alfabeto:
            posicao = alfabeto.find(char)
            nova_posicao = (posicao + chave) % 26
            mensagem_criptografada += alfabeto[nova_posicao]
            chave += 1

    return mensagem_criptografada


def main():
    mensagem = input("Digite a mensagem secreta: ").strip()
    chave = int(input("Digite a chave inicial: ").strip())

    resultado = cifra_avancada(mensagem, chave)
    print("Mensagem super secreta:", resultado)


if __name__ == '__main__':
    main()
