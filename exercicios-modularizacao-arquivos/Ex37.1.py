import os

dir = ''
arq = ''
num = 0

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

def entrada():
    global num
    num = int(input("Digite N: "))
    while num <= 0:
        num = int(input("Valor inválido, digite novamente: "))

def processa():
    global dir, arq, num

    caminho = os.path.join(dir, arq)

    if os.path.exists(caminho):
        os.remove(caminho)

    a, b = 0, 1

    for i in range(num):
        print(a)
        grava(f"{a}\n")
        a, b = b, a + b

def main():
    global dir, arq

    dir = '/tmp/exercicios'
    arq = 'Ex37.1.txt'

    criar_diretorio()
    entrada()
    processa()

main()