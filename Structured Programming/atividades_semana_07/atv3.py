
def movim(sinal):
    if sinal == 'V':
        acao = 'Siga'
    elif sinal == 'A':
        acao = 'Atenção'
    elif sinal == 'E':
        acao = 'Pare'

    return acao


def main():
    # Entrada de dados
    sinal = input('Digite a cor do sinal (V - Verde / A - Amarelo / E - Vermelho): ').strip().upper()

    # Processamento de dados
    acao = movim(sinal)

    # Saída de dados
    print(f'Ação: {acao}')


if __name__ == "__main__":
    main()
