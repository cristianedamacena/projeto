## TRATAMENTO DE STRINGS

def separa_texto_em_caracteres(texto):
    caracteres = []
    for caractere in texto:
        caracteres.append(caractere)
    return caracteres

def verifica_tamanho_chave(entrada):
    binario = bin(int.from_bytes(entrada.encode(), 'big'))[2:]
    binario = binario.zfill(128)
    tamanho_bits = len(binario)
    print("A chave tem: ", tamanho_bits, " bits\n")
    if tamanho_bits != 128:
        return False
    else:
        return True

## MATRIZES

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

def matriz_para_array(matriz):
    array = []
    for linha in matriz:
        for item in linha:
            array.append(item)
    return array

## SBOX

def mapeamemnto_s_box(entrada):
    entrada_array = [caractere for caractere in entrada]
    for i in range (2):
        if (entrada_array[i].isalpha()): 
            entrada_array[i] = int(entrada_array[i], 16)
        else:
            entrada_array[i] = int(entrada_array[i])
    return (s_box_aes_str[entrada_array[0]][entrada_array[1]])

def tratamento_matriz_s_box(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            matriz[i][j] = mapeamemnto_s_box(matriz[i][j])
    return matriz

## SBOX INVERTIDA


def mapememnto_s_box_invertida(entrada):
    entrada_array = [caractere for caractere in entrada]
    for i in range (2):
        if (entrada_array[i].isalpha()): 
            entrada_array[i] = int(entrada_array[i], 16)
        else:
            entrada_array[i] = int(entrada_array[i])
    return (s_box_aes_invertida_str[entrada_array[0]][entrada_array[1]])

## TRATAMENTO DE BLOCOS

def leitura_arquivo_txt(nome_arquivo):
    with open(nome_arquivo, 'r') as arquivo:
        conteudo = arquivo.read()
    return conteudo

def divisao_em_blocos(texto, tamanho_bloco): #Retorna uma lista com todos os blocos criados
    blocos = []
    tamanho_texto = len(texto)
    for i in range(0, tamanho_texto, tamanho_bloco // 8):
        bloco = texto[i:i + (tamanho_bloco // 8)]
        blocos.append(bloco)
    return blocos

def tranferencia_blocos_matriz(blocos):
    array_matrizes = []
    for i in range (len(blocos)):
        matriz = criacao_matriz_vazia(4)
        array_matrizes.append(matriz)
    return array_matrizes

def preenchimento_blocos_matriz(blocos, array_matrizes):
    for i in range (len(blocos)):
        matriz = preenchimento_matriz(array_matrizes[i], blocos[i], 4)
    return array_matrizes

for i, bloco in enumerate(divisao_em_blocos(texto, 128)):
    print(f"Bloco {i + 1}: {bloco}")


hex_value = "1466528872"
byte_value = bytes.fromhex(hex_value)
string_value = byte_value.decode('utf-8')

print(string_value)

## TRATAMENTO DE CHAVES

def aes_key_expansion(key):
    # Tabela de substituição S-box
    sbox = [
        0x63, 0x7c, 0x77, 0x7b, 0xf2, 0x6b, 0x6f, 0xc5, 0x30, 0x01, 0x67, 0x2b, 0xfe, 0xd7, 0xab, 0x76,
        0xca, 0x82, 0xc9, 0x7d, 0xfa, 0x59, 0x47, 0xf0, 0xad, 0xd4, 0xa2, 0xaf, 0x9c, 0xa4, 0x72, 0xc0,
        0xb7, 0xfd, 0x93, 0x26, 0x36, 0x3f, 0xf7, 0xcc, 0x34, 0xa5, 0xe5, 0xf1, 0x71, 0xd8, 0x31, 0x15,
        0x04, 0xc7, 0x23, 0xc3, 0x18, 0x96, 0x05, 0x9a, 0x07, 0x12, 0x80, 0xe2, 0xeb, 0x27, 0xb2, 0x75,
        0x09, 0x83, 0x2c, 0x1a, 0x1b, 0x6e, 0x5a, 0xa0, 0x52, 0x3b, 0xd6, 0xb3, 0x29, 0xe3, 0x2f, 0x84,
        0x53, 0xd1, 0x00, 0xed, 0x20, 0xfc, 0xb1, 0x5b, 0x6a, 0xcb, 0xbe, 0x39, 0x4a, 0x4c, 0x58, 0xcf,
        0xd0, 0xef, 0xaa, 0xfb, 0x43, 0x4d, 0x33, 0x85, 0x45, 0xf9, 0x02, 0x7f, 0x50, 0x3c, 0x9f, 0xa8,
        0x51, 0xa3, 0x40, 0x8f, 0x92, 0x9d, 0x38, 0xf5, 0xbc, 0xb6, 0xda, 0x21, 0x10, 0xff, 0xf3, 0xd2,
        0xcd, 0x0c, 0x13, 0xec, 0x5f, 0x97, 0x44, 0x17, 0xc4, 0xa7, 0x7e, 0x3d, 0x64, 0x5d, 0x19, 0x73,
        0x60, 0x81, 0x4f, 0xdc, 0x22, 0x2a, 0x90, 0x88, 0x46, 0xee, 0xb8, 0x14, 0xde, 0x5e, 0x0b, 0xdb,
        0xe0, 0x32, 0x3a, 0x0a, 0x49, 0x06, 0x24, 0x5c, 0xc2, 0xd3, 0xac, 0x62, 0x91, 0x95, 0xe4, 0x79,
        0xe7, 0xc8, 0x37, 0x6d, 0x8d, 0xd5, 0x4e, 0xa9, 0x6c, 0x56, 0xf4, 0xea, 0x65, 0x7a, 0xae, 0x08,
        0xba, 0x78, 0x25, 0x2e, 0x1c, 0xa6, 0xb4, 0xc6, 0xe8, 0xdd, 0x74, 0x1f, 0x4b, 0xbd, 0x8b, 0x8a,
        0x70, 0x3e, 0xb5, 0x66, 0x48, 0x03, 0xf6, 0x0e, 0x61, 0x35, 0x57, 0xb9, 0x86, 0xc1, 0x1d, 0x9e,
        0xe1, 0xf8, 0x98, 0x11, 0x69, 0xd9, 0x8e, 0x94, 0x9b, 0x1e, 0x87, 0xe9, 0xce, 0x55, 0x28, 0xdf,
        0x8c, 0xa1, 0x89, 0x0d, 0xbf, 0xe6, 0x42, 0x68, 0x41, 0x99, 0x2d, 0x0f, 0xb0, 0x54, 0xbb, 0x16
    ]

    # Tabela de rotação de palavras
    rcon = [
        0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80, 0x1b, 0x36, 0x6c, 0xd8, 0xab, 0x4d, 0x9a, 0x2f
    ]

    # Número de palavras na chave
    nk = len(key) // 4
    print(nk)
    # Número de rodadas
    nr = nk + 6

    # Palavras da chave
    w = [0] * (4 * (nr + 1))
    print(w)

    # Copia a chave para as primeiras palavras
    for i in range(nk):
        w[i] = (key[4*i] << 24) | (key[4*i+1] << 16) | (key[4*i+2] << 8) | key[4*i+3]

    # Gera as palavras adicionais
    for i in range(nk, 4 * (nr + 1)):
        temp = w[i-1]
        if i % nk == 0:
            temp = ((sbox[(temp >> 16) & 0xff] << 24) |
                    (sbox[(temp >> 8) & 0xff] << 16) |
                    (sbox[temp & 0xff] << 8) |
                    sbox[(temp >> 24) & 0xff])
            temp ^= rcon[(i // nk) - 1] << 24
        elif nk > 6 and i % nk == 4:
            temp = (sbox[(temp >> 24) & 0xff] << 24) | \
                   (sbox[(temp >> 16) & 0xff] << 16) | \
                   (sbox[(temp >> 8) & 0xff] << 8) | \
                   sbox[temp & 0xff]
        w[i] = w[i-nk] ^ temp

    # Retorna as palavras da chave expandida
    return w


#key = [0x2b, 0x7e, 0x15, 0x16, 0x28, 0xae, 0xd2, 0xa6, 0xab, 0xf7, 0x15, 0x88, 0x09, 0xcf, 0x4f, 0x3c]

key_string = "bomdiabrasilllll"
key = []
for char in key_string:
    key.append(ord(char))

expanded_key = aes_key_expansion(key)
key_hex = ''.join([hex(x)[2:].zfill(2) for x in key])
print(key_hex)
print(expanded_key)

## TRATAMENTO DE HEXADECIMAL

def calcula_xor_entre_hexadecimais(hex1, hex2):
    bin1 = bin(int(hex1, 16))[2:].zfill(len(hex1) * 4)
    bin2 = bin(int(hex2, 16))[2:].zfill(len(hex2) * 4)
    resultado_xor = int(bin1, 2) ^ int(bin2, 2)
    resultado_hex = hex(resultado_xor)[2:]
    if len(resultado_hex) == 1:
        resultado_hex = "0" + resultado_hex
    return resultado_hex

def transforma_char_para_hexadecimal(caractere):
    valor_hex = hex(ord(caractere))
    return hex(int(valor_hex.lower(),16))

def transformacao_string_para_hex_formatado(caractere):
    valor_decimal = ord(caractere) 
    valor_hex = hex(valor_decimal)  
    return format(valor_hex, '02x')

def transforma_char_para_hexadecimal_formatado(caractere):
    valor_hex = hex(ord(caractere))[2:]
    return valor_hex.lower()


def hexadecimal_para_string(hexadecimal):
    # Remover o prefixo '0x', se presente
    if hexadecimal[:2] == '0x':
        hexadecimal = hexadecimal[2:]

    # Converter hexadecimal em bytes e decodificar em string
    byte_object = bytes.fromhex(hexadecimal)
    string = byte_object.decode('utf-8')
    return string


def verifica_tamanho_chave(entrada):
    binario = bin(int.from_bytes(entrada.encode(), 'big'))[2:]
    binario = binario.zfill(128)
    tamanho_bits = len(binario)
    print("A chave tem: ", tamanho_bits, " bits\n")
    if tamanho_bits < 128:
        # Se a chave for menor que 128 bits, completa com 0x00
        binario = binario.ljust(128, '0')
        tamanho_bits = len(binario)
        print("A chave foi completada para: ", tamanho_bits, " bits\n")
    decimal = binario_para_decimal(binario)
    hexadecimal = decimal_para_hexadecimal(decimal)

    return hexadecimal



def verifica_tam_chave(chave_original):
    chave_bin = bin(chave_original)[2:]
    if len(chave_bin) < 128:
        chave_bin = chave_bin.ljust(128, '0') # Se a chave for menor que 128 bits, completa com 0x00

    chave_verificada = int(chave_bin, 2)
    return chave_verificada


def binario_para_decimal(binario):
    decimal = 0
    for i in range(len(binario)):
        if binario[i] == '1':
            decimal += 2 ** (len(binario) - 1 - i)
    return decimal




def decimal_para_hexadecimal(decimal):
    hexadecimal = hex(decimal).upper()[2:]
    return hexadecimal
