
# ==================================================
# FUNÇÃO PRINCIPAL
# ==================================================

def main():
    # Entrada de dados
    nascimento = int(input("Digite sua data de nascimento no formato DDMMAAAA: "))

    # Separa a data e identifica o signo
    dia, mes, _ = separar_data(nascimento)
    meu_signo = signo(dia, mes)

    # Busca o horóscopo do signo encontrado
    horoscopo_de_hoje = horoscopo(meu_signo)

    # Mostra o resultado
    print(horoscopo_de_hoje)


# ==================================================
# SEPARA A DATA DE NASCIMENTO
# ==================================================

def separar_data(dma):
    # Pega os quatro últimos dígitos, que representam o ano
    a = dma % 10000
    dma //= 10000

    # Pega os dois últimos dígitos restantes, que representam o mês
    m = dma % 100
    dma //= 100

    # O que sobrou representa o dia
    d = dma

    # Retorna o dia, o mês e o ano
    return d, m, a


# ==================================================
# IDENTIFICA O SIGNO
# ==================================================

def signo(dia, mes):

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


# ==================================================
# REMOVE OS ACENTOS DO TEXTO
# ==================================================

def remover_acentos(texto):
    from unicodedata import normalize

    # Converte caracteres acentuados para caracteres sem acento
    return normalize('NFKD', texto).encode(
        'ASCII', 'ignore'
    ).decode('ASCII')


# ==================================================
# BUSCA O HORÓSCOPO NO SITE
# ==================================================

def horoscopo(signo_desejado):
    import urllib.request

    # Deixa o nome do signo sem acentos e em letras minúsculas
    signo_formatado = remover_acentos(signo_desejado).lower()

    # Monta o endereço da página do signo
    minha_url = 'https://www.horoscopovirtual.com.br/horoscopo/' + signo_formatado

    # Cria a requisição para acessar o site
    requisicao = urllib.request.Request(
        url=minha_url,
        headers={'User-Agent': 'Mozilla/5.0'}
    )

    # Envia a requisição e recebe a resposta
    resposta = urllib.request.urlopen(requisicao)

    # Lê o conteúdo da página como texto
    pagina = resposta.read().decode('utf-8')

    # Define os trechos usados para localizar o horóscopo
    marcador_inicio = '<p class="text-pred">'
    marcador_final = '</p>'

    # Encontra onde começa o texto desejado
    inicio = pagina.find(marcador_inicio) + len(marcador_inicio)

    # Encontra onde termina o parágrafo
    final = pagina.find(marcador_final, inicio)

    # Retorna o signo junto com o texto encontrado
    return signo_desejado + ': ' + pagina[inicio:final]


# ==================================================
# EXECUÇÃO DO PROGRAMA
# ==================================================

# Executa main() quando este arquivo é iniciado diretamente
if __name__ == '__main__':
    main()
