
def main():
    # Lê a data de nascimento digitada pelo usuário
    nascimento = int(input("Digite sua data de nascimento: "))

    # Separa a data em dia, mês e ano
    dia, mes, ano = separar_data(nascimento)

    # Descobre o signo com base no dia e no mês
    meu_signo = signo(dia, mes)

    # Busca o horóscopo correspondente ao signo
    texto = horoscopo(meu_signo)

    # Mostra o resultado na tela
    print(texto)


def separar_data(dma):
    # Pega os quatro últimos números, que representam o ano
    ano = dma % 10000

    # Retira o ano, deixando apenas o dia e o mês
    dma //= 10000

    # Pega os dois últimos números, que representam o mês
    mes = dma % 100

    # O que sobrou é o dia
    dma //= 100
    dia = dma

    # Retorna as três partes da data
    return dia, mes, ano


def signo(dia, mes):
    # Verifica o signo de acordo com o mês e o dia
    if mes == 3:
        return 'Peixes' if dia < 21 else 'Áries'

    if mes == 4:
        return 'Áries' if dia < 20 else 'Touro'

    if mes == 5:
        return 'Touro' if dia < 21 else 'Gêmeos'

    if mes == 6:
        return 'Gêmeos' if dia < 22 else 'Câncer'

    if mes == 7:
        return 'Câncer' if dia < 23 else 'Leão'

    if mes == 8:
        return 'Leão' if dia < 23 else 'Virgem'

    if mes == 9:
        return 'Virgem' if dia < 23 else 'Libra'

    if mes == 10:
        return 'Libra' if dia < 23 else 'Escorpião'

    if mes == 11:
        return 'Escorpião' if dia < 22 else 'Sagitário'

    if mes == 12:
        return 'Sagitário' if dia < 22 else 'Capricórnio'

    if mes == 1:
        return 'Capricórnio' if dia < 20 else 'Aquário'

    if mes == 2:
        return 'Aquário' if dia < 19 else 'Peixes'


def remover_acentos(texto):
    from unicodedata import normalize

    # Remove os acentos para facilitar a montagem da URL
    return normalize('NFKD', texto).encode(
        'ASCII', 'ignore'
    ).decode('ASCII')


def horoscopo(signo_desejado):
    import urllib.request

    # Deixa o nome do signo sem acentos e em letras minúsculas
    signo_formatado = remover_acentos(signo_desejado).lower()

    # Monta o endereço da página do horóscopo
    minha_url = (
        'https://www.horoscopovirtual.com.br/horoscopo/'
        + signo_formatado
    )

    # Faz a requisição para acessar o site
    requisicao = urllib.request.Request(
        url=minha_url,
        headers={'User-Agent': 'Mozilla/5.0'}
    )

    resposta = urllib.request.urlopen(requisicao)

    # Lê o HTML que o site devolveu
    pagina = resposta.read().decode('utf-8')

    # Procura o trecho onde começa o texto do horóscopo
    marcador_inicio = '<p class="text-pred">'
    marcador_final = '</p>'

    inicio = pagina.find(marcador_inicio) + len(marcador_inicio)
    final = pagina.find(marcador_final, inicio)

    # Pega somente o texto entre os dois marcadores
    return signo_desejado + ': ' + pagina[inicio:final]


# Executa o programa principal quando este arquivo é iniciado
if __name__ == '__main__':
    main()
