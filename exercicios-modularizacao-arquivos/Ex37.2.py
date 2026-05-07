import os

dir = '/tmp/exercicios'
arq = 'Ex37.1.txt'

def verificar_impar(num):
    if num % 2 != 0:
        return num
    return -1

def ler_arquivo():
    caminho = os.path.join(dir, arq)

    with open(caminho, 'r') as file:
        for linha in file:
            num = int(linha.strip())
            resultado = verificar_impar(num)

            if resultado != -1:
                print(resultado)

ler_arquivo()