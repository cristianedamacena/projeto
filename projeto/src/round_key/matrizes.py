from hexadecimal import transforma_char_para_hexadecimal
from sub_bytes.sbox import mapeamemnto_s_box
from hexadecimal import calcula_xor_entre_hexadecimais

def criacao_matriz_vazia(tamanho):
    return [[None for _ in range(tamanho)] for _ in range(tamanho)]

def preenchimento_matriz(matriz, texto):
    k = 0
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            if k < len(texto):
                matriz[i][j] = texto[k]
                k += 1
    return matriz

def transforma_matriz_para_hex(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            matriz[i][j] = transforma_char_para_hexadecimal(matriz[i][j])
    return matriz

def tratamento_matriz_s_box(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            matriz[i][j] = mapeamemnto_s_box(matriz[i][j])
    return matriz

def impressao_matriz(matriz):
    for linha in matriz:
        print(linha)       

def impressao_matriz_formatada(matriz, matriz_formatada):
    for j in range(16):
        matriz[i][j] = (format(matriz_formatada[i][j], '02x'))
    print()

def calcula_xor_entre_matrizes(matriz1, matriz2):
    matriz_resultado = criacao_matriz_vazia(4)
    for i in range(len(matriz1)):
        for j in range(len(matriz1)):
            matriz_resultado[i][j] = calcula_xor_entre_hexadecimais(matriz1[i][j], matriz2[i][j])
    return matriz_resultado