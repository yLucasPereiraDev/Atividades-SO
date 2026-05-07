import os

#Variáveis globais
valor: int = 0
dir: str = ''
arq: str = ''

def criar_diretorio():
    global dir

    if not os.path.exists(dir):
        os.makedirs(dir)

    os.chmod(dir, 0o744)

def mult(vlr, tab):
    res = vlr * tab
    return res

def grava(c, rslt):
    global dir, arq

    file = ""
    tipo = ""
    enc = ""
    linha = str(rslt) + '\n'

    if os.path.exists(dir) and os.path.isdir(dir):

        caminho = os.path.join(dir, arq)

        # Define tipo de escrita
        if os.path.exists(caminho) and c > 0:
            tipo = 'a'
        else:
            tipo = 'w'

        with open(caminho, tipo) as file:
            file.write(linha)

def main():
    global valor, dir, arq

    contador = 1
    result = 0

    dir = '/tmp/exercicios'
    arq = 'Ex34.txt'

    criar_diretorio()

    valor = int(input("Digite um valor entre 1 e 10: "))

    while contador <= 10:
        result = mult(valor, contador)
        print(f"{contador} x {valor} = {result}")

        grava(contador, result)

        contador += 1

main()
