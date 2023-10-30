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
