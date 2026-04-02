import os

#Variáveis globais
nome: str = ''
nota1: float = 0
nota2: float = 0
nota3: float = 0
nota4: float = 0
valor_media: float = 0
dir: str = ''
arq: str = ''

def criar_diretorio():
    global dir

    if not os.path.exists(dir):
        os.makedirs(dir)

    os.chmod(dir, 0o744)

def med(n1, n2, n3, n4):
    media = (n1 + n2 + n3 + n4) / 4
    return media


def escreveArq(caminho, arquivo, linha_arq):
    file = ""
    tipo = ""
    enc = ""

    if os.path.exists(caminho) and os.path.isdir(caminho):

        caminho_arquivo = os.path.join(caminho, arquivo)

        if os.path.exists(caminho_arquivo):
            tipo = 'a'
        else:
            tipo = 'w'

        with open(caminho_arquivo, tipo) as file:
            file.write(linha_arq)


def cadastro(nm, nt1, nt2, nt3, nt4, vlr_med):
    global dir, arq

    linha = (
        nm + ":" +
        str(nt1) + ";" +
        str(nt2) + ";" +
        str(nt3) + ";" +
        str(nt4) + ";" +
        str(vlr_med) + "\n"
    )

    escreveArq(dir, arq, linha)


def entrada():
    global nome, nota1, nota2, nota3, nota4, valor_media

    nome = input("Digite o nome do aluno: ")
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    nota3 = float(input("Nota 3: "))
    nota4 = float(input("Nota 4: "))

    valor_media = med(nota1, nota2, nota3, nota4)

    print(f"Média de {nome}: {valor_media}")

    cadastro(nome, nota1, nota2, nota3, nota4, valor_media)


def main():
    global dir, arq

    contador = 1

    dir = '/tmp/exercicios'
    arq = 'Ex21.txt'

    criar_diretorio()

    while contador <= 5:
        entrada()
        contador += 1

main()