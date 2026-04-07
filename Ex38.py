import os

dir: str = ''
arq: str = ''

def criar_diretorio():
    global dir

    if not os.path.exists(dir):
        os.makedirs(dir)

    os.chmod(dir, 0o744)

def grava(linha):
    global dir, arq

    caminho = os.path.join(dir,arq)

    if os.path.exists(caminho):
        tipo = 'a'
    else:
        tipo = 'w'

    with open(caminho, tipo) as file:
        file.write(linha)

def main():
    global dir, arq

    dir = '/tmp/exercicios'
    arq = 'Ex38.txt'

    criar_diretorio()

    caminho = os.path.join(dir,arq)
    if os.path.exists(caminho):
        os.remove(caminho)

    num = float(input('Digite o primeiro número: '))
    while num < 0:
        num = float(input('Número  inválido, digite algo maior que 0: '))
    
    maior = num
    menor = num

    grava(f'{num}\n')

    for i in range(2, 101):
        num = float(input('Digite o segundo número: '))
        while num < 0:
            num = float(input('Número  inválido, digite algo maior que 0: '))

        grava(f'{num}\n')

        if num > maior:
            maior = num
        if num < menor:
            menor = num
    
    grava(f'\nMaior valor: {maior}\n')
    grava(f'\nMenor valor: {menor}\n')

    print('Maior Valor: ', maior)
    print('Menor Valor: ', menor)

main()