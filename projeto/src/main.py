import sys
from bloco import divisao_em_blocos
from bloco import leitura_arquivo_txt
from bloco import tranferencia_blocos_matriz
from config import verifica_tamanho_chave
from round_key.matrizes import criacao_matriz_vazia
from config import separa_texto_em_caracteres
from round_key.matrizes import preenchimento_matriz
from round_key.matrizes import transforma_matriz_para_hex
from sub_bytes.sbox import tratamento_matriz_s_box
from round_key.matrizes import calcula_xor_entre_matrizes

print(f"\nEste é um projeto de criptografia\n")

# print(f"Coloque o texto que deseja usar como entrada dentro do arquivo input.txt\n")
# while True:
#     entrada = input("O texto desejado já está gravado dentro to txt?\n\nPressione 'y' para SIM e 'n' para NÃO:\n\n")
#     print("\n")
#     if entrada.lower() == 'y':
#         break
#     else:
#         print(f"\nSalve o texto desejado no arquivo imput.txt na raiz do projeto e execute o programa novamente\n") 
#         sys.exit()

# while True:
#     chave = input("Entre com a chave desejada.\n\nO tamanho deve ser de exatamente 128 bits:\n\n")
#     print("\n")
#     if verifica_tamanho_chave(chave):
#         break

print("\n######### RODADA INCIAL - 0 #########\n")

chave = 'bomdiabrasilllll'
texto = leitura_arquivo_txt('src/input.txt')
matriz_texto = criacao_matriz_vazia(4)
matriz_chave = criacao_matriz_vazia(4)
texto_separado = separa_texto_em_caracteres(texto)
chave_separada = separa_texto_em_caracteres(chave)
matriz_texto = preenchimento_matriz(matriz_texto, texto_separado)
matriz_chave = preenchimento_matriz(matriz_chave, chave_separada)
transforma_matriz_para_hex(matriz_chave)
transforma_matriz_para_hex(matriz_texto)

print("\n######### ROUND - 0 #########\n")

print("\n######### ADD ROUND KEY - 0 #########\n")

matriz_resultado = calcula_xor_entre_matrizes(matriz_chave, matriz_texto)
print(matriz_resultado)

print("\n######### RODADA - 1 #########")

print("\n######### SUB BYTES #########\n")

print(tratamento_matriz_s_box(matriz_resultado))

print("\n######### SHIFT ROWS #########\n")

print(tratamento_matriz_s_box(matriz_resultado))

print("\n######### MIX COLUMNS #########\n")

print(tratamento_matriz_s_box(matriz_resultado))

print("\n######### ADD ROUND KEY #########\n")

print(tratamento_matriz_s_box(matriz_resultado))

input()
