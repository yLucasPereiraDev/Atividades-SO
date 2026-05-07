import os

dir = ''
arq = ''

def criar_diretorio():
    global dir
    if not os.path.exists(dir):
        os.makedirs(dir)
    os.chmod(dir, 0o744)

def grava(linha):
    global dir, arq
    caminho = os.path.join(dir, arq)

    with open(caminho, 'a') as file:
        file.write(linha)

def processa():
    global dir, arq

    caminho = os.path.join(dir, arq)

    # apagar arquivo se existir
    if os.path.exists(caminho):
        os.remove(caminho)

    for num in range(10, 151):
        quadrado = num ** 2
        linha = f"{num}^2 = {quadrado}\n"
        print(linha.strip())
        grava(linha)

def main():
    global dir, arq

    dir = '/tmp/exercicios'
    arq = 'Ex31.1.txt'

    criar_diretorio()
    processa()

main()