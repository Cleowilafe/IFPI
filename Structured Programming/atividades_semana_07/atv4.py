def analise(caract):
    if caract in 'a,e, i, o, u, A, E, I, O, U':
        tipo = 'vogal'
    elif caract in 'b, c, d, f, g, h, j, k, l, m, n, p, q, r, s, t, v, w, x, y, z, B, C, D, F, G, H, J, K, L, M, N, P, Q, R, S, T, V, W, X, Y, Z':
        tipo = 'consoante'
    elif caract in '0, 1, 2, 3, 4, 5, 6, 7, 8 ,9':
        tipo = 'número'
    else:
        tipo = 'símbolo'

    return tipo


def main():
    # Entrada de dados
    caract = input('Digite um caractere: ')

    # Processamento de dados
    tipo = analise(caract)

    # Saída de dados
    print(f'O caractere informado é: {tipo}')


if __name__ == "__main__":
    main()
