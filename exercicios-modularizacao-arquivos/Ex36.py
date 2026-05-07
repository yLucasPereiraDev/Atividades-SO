import os

dir: str = ''
arq: str = ''
num: int = 0

def criar_diretorio():
    global dir

    if not os.path.exists(dir):
        os.makedirs(dir)

    os.chmod(dir, 0o744)

def grava(linha):
    global dir, arq

    caminho = os.path.join(dir, arq)

    if os.path.exists(caminho):
        tipo = 'a'
    else:
        tipo = 'w'

    with open(caminho, tipo) as file:
        file.write(linha)

def entrada():
    global num

    num = int(input("Digite um número: "))
    while num <= 0:
        num = int(input("Número inválido, digite um valor maior que 0: "))

def fatorial(n):
    fat = 1
    for i in range(1, n + 1):
        fat *= i
    return fat

def divisao(valor):
    return 1 / valor

def processa():
    global num

    soma = 1

    grava("Termos da série:\n")
    grava("1\n")

    for i in range(1, num + 1):
        fat = fatorial(i)
        termo = divisao(fat)

        grava(f"1/{fat} = {termo:.6f}\n")

        soma += termo

    grava(f"\nResultado final: {soma:.2f}\n")

    print(f"Resultado da série: {soma:.2f}")

def main():
    global dir, arq

    dir = '/tmp/exercicios'
    arq = 'Ex36.txt'

    criar_diretorio()

    caminho = os.path.join(dir, arq)
    if os.path.exists(caminho):
        os.remove(caminho)

    entrada()
    processa()

main()