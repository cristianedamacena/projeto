def impressao_matriz_formatada(matriz, matriz_formatada):
    for j in range(16):
        matriz[i][j] = (format(matriz_formatada[i][j], '02x'))
    print()

def impressao_matriz(matriz):
    for linha in matriz:
        print(linha)

def criacao_matriz_vazia(tamanho):
    return [[None for _ in range(tamanho)] for _ in range(tamanho)]

def preenchimento_matriz(matriz, texto, tamanho):
    for i in range(tamanho):
        for j in range(tamanho):
            matriz[i][j] = texto[i + (j * tamanho)]
    return matriz

def transformacao_string_para_hex(caractere):
    valor_decimal = ord(caractere) 
    valor_hex = hex(valor_decimal)  
    return valor_hex

def transformacao_string_para_hex_formatado(caractere):
    valor_decimal = ord(caractere) 
    valor_hex = hex(valor_decimal)  
    return format(valor_hex, '02x')
