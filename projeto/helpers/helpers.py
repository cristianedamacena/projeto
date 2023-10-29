def impressao_matriz_formatada(matriz, matriz_formatada):
    for j in range(16):
        matriz[i][j] = (format(matriz_formatada[i][j], '02x'))
    print()

def impressao_matriz(matriz):
    for linha in matriz:
        print(linha)