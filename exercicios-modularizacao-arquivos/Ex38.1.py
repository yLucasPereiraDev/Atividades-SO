import os

dir: str = ''
arq: str = ''
arq2: str = ''

def criar_diretorio():
    global dir

    if not os.path.exists(dir):
        os.makedirs(dir)

    os.chmod(dir, 0o744)

def grava(linha):
    global dir, arq2

    caminho = os.path.join(dir, arq2)

    if os.path.exists(caminho):
        tipo = 'a'
    else:
        tipo = 'w'

    with open(caminho, tipo) as file:
        file.write(linha)

def leitura_processa():
    global dir, arq

    caminho = os.path.join(dir, arq)

    with open(caminho, 'r') as file:
        for linha in file:
            linha = linha.strip()

            if linha == '':
                continue

            if 'Maior' in linha or 'Menor' in linha:
                continue

            num = int(float(linha))

            if num % 5 == 0:
                grava(f'{num}\n')

def main():
    global dir, arq, arq2

    dir = '/tmp/exercicios'
    arq = 'Ex38.txt'
    arq2 = 'multiplos5.txt'

    criar_diretorio()

    caminho_saida = os.path.join(dir, arq2)

    if os.path.exists(caminho_saida):
        os.remove(caminho_saida)

    leitura_processa()

    print('Processamento concluído')
    print('Arquivo gerado com múltiplos de 5')

main()