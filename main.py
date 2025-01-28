import sys

def JDcrc16(dados: bytes, path: str = "resultado.txt"):
    #Definindo os valores padrões para o cálculo
    #CRC-CCITT (0xFFFF)
    crc = 0xFFFF
    polinomial = 0x1021
    
    for byte in dados:
        
        crc ^= (byte << 8)
        for _ in range(8):
            if crc & 0x8000:
                crc = (crc << 1) ^ polinomial
            else:
                crc <<= 1
            crc &= 0xFFFF
    
    #Salvando o resultado do processamento no arquivo de saída
    with open (path, "w") as arquivo:
        arquivo.write(f"{crc:04X}")   


#Validando o número máximo de parâmetros necessários para execução da função.
if len(sys.argv) != 3:
    print("Este programa precisa de 02 parâmetros para execução! \n Parâmetro 01: dados \n Parâmetro 02: caminho completo para retorno do processamento.")
    sys.exit(1)

#Captando as informações de entrada
dados_para_processar = sys.argv[1].encode("utf-8")
caminho_para_salvar_resposta = sys.argv[2]

#Executando a função
JDcrc16(dados_para_processar, caminho_para_salvar_resposta)

#Fim
sys.exit(1)
