# Funções relativas à manipulação dos blocos

from round_key.matrizes import criacao_matriz_vazia
from round_key.matrizes import preenchimento_matriz

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



# # Exibir os blocos resultantes
# for i, bloco in enumerate(divisao_em_blocos(texto, 128)):
#     print(f"Bloco {i + 1}: {bloco}")