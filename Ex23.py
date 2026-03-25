n1 = 0
n2 = 0
n3 = 0
n4 = 0
lista = [] # cria uma lista vazia
tipo = 0

def entrada():
    global n1, n2, n3, n4
    n1 = int(input("Digite o primeiro número: "))
    n2 = int(input("Digite o segundo número: "))
    n3 = int(input("Digite o terceiro número: "))
    n4 = int(input("Digite o quarto número: "))

def processamento():
    global n1, n2, n3, n4, lista, tipo

    if n1 <= n2 <= n3:
        tipo = 1
        lista = [n1, n2, n3, n4] # lista com valores
        lista.sort() #sort() - organiza a lista em ordem crescente
    else:
        tipo = 2

def saida():
    global lista, tipo
    if tipo == 2:
        print("Os 3 primeiros números não estão em ordem crescente.")
    else:
        print("Ordem crescente:", lista)

def main():
    entrada()
    processamento()
    saida()

main()

