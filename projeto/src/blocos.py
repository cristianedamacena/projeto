def divisao_em_blocos(texto, tamanho_bloco=128):
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



