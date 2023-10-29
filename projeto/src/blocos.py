#Conjunto de ações para tratamento de blocos
from helpers.helpers import criacao_matriz_vazia

def divisao_em_blocos(texto, tamanho_bloco):
    blocos = []
    tamanho_texto = len(texto)
    for i in range(0, tamanho_texto, tamanho_bloco // 8):
        bloco = texto[i:i + (tamanho_bloco // 8)]
        blocos.append(bloco)
    return blocos

def leitura_arquivo_txt(nome_arquivo):
    with open(nome_arquivo, 'r') as arquivo:
        conteudo = arquivo.read()
    return conteudo

texto = 'Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industrys standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.'

print(divisao_em_blocos(texto, 128))
print(len(divisao_em_blocos(texto, 128)))

# Exibir os blocos resultantes
for i, bloco in enumerate(divisao_em_blocos(texto, 128)):
    print(f"Bloco {i + 1}: {bloco}")

criacao_matriz_vazia(4)