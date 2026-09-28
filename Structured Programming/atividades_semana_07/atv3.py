def movim(sinal):
    if sinal == 'V':
        acao = 'Siga'
    elif sinal == 'A':
        acao = 'Atenção'
    elif sinal == 'E':
        acao = 'Pare'
    return acao

def main():
#Entrada de dados
    sinal = input().strip().upper()
#Processamento de dados
    acao = movim(sinal)
#Saida de dados
    print(acao)
    
if __name__ == "__main__":
    main()