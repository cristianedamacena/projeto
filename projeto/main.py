import sys
from blocos import divisao_em_blocos
from blocos import leitura_arquivo_txt
from blocos import tranferencia_blocos_matriz

print(f"\nEste é um projeto de criptografia\n")
print(f"Coloque o texto que deseja usar como entrada dentro do arquivo input.txt\n")

while True:
    entrada = input("O texto desejado já está gravado dentro to txt?\n\nPressione 'y' para SIM e 'n' para NÃO: \n\n")
    print("\n")
    if entrada.lower() == 'y':
        break
    else:
        print(f"\nSalve o texto desejado no arquivo imput.txt na raiz do projeto e execute o programa novamente\n") 
        sys.exit()
      
texto = leitura_arquivo_txt('input.txt')
blocos_dividos = divisao_em_blocos(texto, 128)
print(tranferencia_blocos_matriz(blocos_dividos))

input()