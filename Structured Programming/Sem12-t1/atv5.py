def simular_populacao_dodo(populacao_inicial):
    populacao = populacao_inicial
    limite_extincao = populacao_inicial * 0.10
    ano = 1600

    while populacao >= limite_extincao:
        nascimentos = populacao * 0.01
        mortes = populacao * 0.06
        populacao = populacao + nascimentos - mortes
        print(f'{ano},{round(nascimentos)},{round(mortes)},{round(populacao)}')
        ano += 1


def main():
    populacao_1600 = float(input().strip())
    simular_populacao_dodo(populacao_1600)


if __name__ == '__main__':
    main()
