def calcula_xor_entre_hexadecimais(hex1, hex2):
    bin1 = bin(int(hex1, 16))[2:].zfill(len(hex1) * 4)
    bin2 = bin(int(hex2, 16))[2:].zfill(len(hex2) * 4)
    resultado_xor = int(bin1, 2) ^ int(bin2, 2)
    resultado_hex = hex(resultado_xor)[2:]
    if len(resultado_hex) == 1:
        resultado_hex = "0" + resultado_hex
    return resultado_hex

def transforma_char_para_hexadecimal(caractere):
    valor_hex = hex(ord(caractere))[2:]
    return valor_hex.lower()

def transformacao_string_para_hex_formatado(caractere):
    valor_decimal = ord(caractere) 
    valor_hex = hex(valor_decimal)  
    return format(valor_hex, '02x')