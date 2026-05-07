n1 = 0
n2 = 0
maior = 0
menor = 0
tipo = 0

def entrada():
    global n1, n2
    n1 = int(input("Digite o primeiro número: "))
    n2 = int(input("Digite o segundo número: "))

def processamento():
    global n1, n2, maior, menor, tipo

    if n1 > n2:
        maior = n1
        menor = n2
    else:
        maior = n2
        menor = n1

    if maior % menor == 0:
        tipo = 1
    else:
        tipo = 2

def saida():
    global tipo
    if tipo == 1:
        print("O maior é múltiplo do menor!")
    else:
        print("O maior não é múltiplo do menor!")

def main():
    entrada()
    processamento()
    saida()

main()
