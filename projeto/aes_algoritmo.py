import sys
import time


def transforma_char_para_hexadecimal(caractere):
    valor_hex = hex(ord(caractere))
    return hex(int(valor_hex.lower(),16))

def barra_de_progresso(percentual, comprimento=30):
    preenchimento = int(comprimento * percentual)
    barra = '=' * preenchimento + '-' * (comprimento - preenchimento)
    sys.stdout.write(f'\r[{barra}] {int(percentual * 100)}%')
    sys.stdout.flush()

def transforma_texto_para_binario(texto):
    return ''.join(format(ord(i), '08b') for i in texto)

def tratamento_chave_hexa(chave):
    chave_hex = chave.encode("utf-8").hex()
    return chave_hex

def transforma_texto_para_array_int(texto):
    array_int = []
    for char in texto:
        array_int.append(ord(char))
    return array_int

def transforma_para_array_hexa(chave):
    array_hexa = [chave[i:i+2] for i in range(0, len(chave), 2)]
    return array_hexa

def leitura_arquivo_txt(nome_arquivo):
    with open(nome_arquivo, 'r') as arquivo:
        conteudo = arquivo.read()
    return conteudo

def matrix2text(matrix):
    text = 0
    for i in range(4):
        for j in range(4):
            text |= (matrix[i][j] << (120 - 8 * (4 * i + j)))
    return text

def rodadas(chave):
    palavras_na_chave = len(chave) // 4
    return palavras_na_chave + 6

def expande_chave(chave_original):
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

    rcon = [
        0x8d, 0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80, 0x1b, 0x36, 0x6c, 0xd8, 0xab, 0x4d, 0x9a, 0x2f
    ]

    palavras_na_chave = len(chave_original) // 4

    numero_rodadas = rodadas(chave_original)

    print("\nPara esta chave, o numero de rodadas é: ", numero_rodadas)

    palavras_expandidas = [0] * (4 * (numero_rodadas + 1))

    for i in range(palavras_na_chave):
        palavras_expandidas[i] = (chave_original[2*i] << 8) | chave_original[2*i+1]

    for i in range(palavras_na_chave, 4 * (numero_rodadas + 1)):
        temp = palavras_expandidas[i-1]
        if i % palavras_na_chave == 0:
            temp = ((sbox[(temp >> 8) & 0xff] << 8) | sbox[temp & 0xff])
            temp ^= rcon[(i // palavras_na_chave) - 1]
        elif palavras_na_chave > 6 and i % palavras_na_chave == 4:
            temp = (sbox[(temp >> 8) & 0xff] << 8) | sbox[temp & 0xff]
        palavras_expandidas[i] = palavras_expandidas[i-palavras_na_chave] ^ temp

    return palavras_expandidas

def criacao_matriz_vazia(tamanho):
    return [[None for _ in range(tamanho)] for _ in range(tamanho)]

def separa_texto_em_caracteres(texto):
    caracteres = []
    for caractere in texto:
        caracteres.append(caractere)
    return caracteres

def preenchimento_matriz(matriz, texto):
    k = 0
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            if k < len(texto):
                matriz[i][j] = texto[k]
                k += 1
    return matriz

def divisao_em_blocos(texto, tamanho_bloco): #Retorna uma lista com todos os blocos criados
    blocos = []
    tamanho_texto = len(texto)
    for i in range(0, tamanho_texto, tamanho_bloco // 8):
        bloco = texto[i:i + (tamanho_bloco // 8)]
        blocos.append(bloco)
    return blocos

def preenchimento_blocos_matriz(blocos, array_matrizes):
    for i in range (len(blocos)):
        matriz = preenchimento_matriz(array_matrizes[i], blocos[i])
    return matriz

def tranferencia_blocos_matriz(blocos):
    array_matrizes = []
    for i in range (len(blocos)):
        matriz = criacao_matriz_vazia(4)
        preenchimento_matriz(matriz, blocos[i])
        array_matrizes.append(matriz)
    return array_matrizes

def imprime_matriz(matriz):
    for linha in matriz:
        for valor in linha:
            print(valor, end=" ")
        print()

def transforma_matriz_para_hex(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            matriz[i][j] = transforma_char_para_hexadecimal(matriz[i][j])
    return matriz

def calcula_xor_entre_hexadecimais(hex1, hex2):
    bin1 = bin(int(hex1, 16))[2:].zfill(len(hex1) * 4)
    bin2 = bin(int(hex2, 16))[2:].zfill(len(hex2) * 4)
    resultado_xor = int(bin1, 2) ^ int(bin2, 2)
    resultado_hex = hex(resultado_xor)[2:]
    if len(resultado_hex) == 1:
        resultado_hex = "0" + resultado_hex
    return resultado_hex

def calcula_xor_entre_matrizes(matriz1, matriz2, count):
    matriz_resultado = criacao_matriz_vazia(4)
    for i in range(len(matriz1)):
        for j in range(len(matriz1)):
            matriz_resultado[i][j] = calcula_xor_entre_hexadecimais(matriz1[count][i][j], matriz2[i][j])
    return matriz_resultado

def adiciona_chave_rodada(bloco_atual, chave_atual, count):
    for i in range(4):
        for (j) in range(4):
            bloco_atual[i][j] ^= chave_atual[i][j]

def criptografa_aes(texto, chave):
    #contador de rodadas
    count = 0
    #tratamento da chave
    chave_array = transforma_texto_para_array_int(chave)
    chave_expandida = expande_chave(chave_array)
    numero_rodadas = rodadas(chave_array)
    #tratamento do bloco
    blocos_dividos = divisao_em_blocos(texto, 128)
    array_matrizes = tranferencia_blocos_matriz(blocos_dividos)
    #transforma em hexadecimal
    matriz_hex = transforma_matriz_para_hex(array_matrizes[0])
    chave_expandida_hex = ([hex(x)[2:].zfill(2) for x in chave_expandida])
    

print(f"\nEste é um projeto de criptografia\n")
print(f"Coloque o texto que deseja usar como entrada para criptografia dentro do arquivo input.txt\n")
while True:
    entrada = input("O texto desejado já está gravado dentro to txt?\n\nPressione 'y' para SIM e 'n' para NÃO:\n\n")
    print("\n")
    if entrada.lower() == 'y':
        break
    else:
        print(f"\nSalve o texto desejado no arquivo imput.txt na raiz do projeto e execute o programa novamente\n") 
        sys.exit()


chave = input("Entre com a chave desejada:\n\n")
texto = leitura_arquivo_txt('input.txt')

print("\n")

print(f"\nA chave já foi expandida conforme o número de rodadas\n") 

input()

print("\n######### COMEÇANDO A CRIPTOGRAFIA #########\n")

criptografa_aes(texto, chave)