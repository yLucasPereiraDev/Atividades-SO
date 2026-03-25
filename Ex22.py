n1 = 0
n2 = 0
menor = 0
maior = 0
tipo = 0

def entrada():
    global n1, n2
    n1 = int(input("Digite o valor do primeiro número: ")) 
    n2 = int(input("Digite o valor do segundo número: "))

def processamento():
    global n1, n2, menor, maior, tipo
    if n1 == n2:
        tipo = 1 #Erro, números iguais
    else:
        tipo = 2
        if n1 > n2:
            maior = n1
            menor = n2
        else:
            maior = n2
            menor = n1


def saida():
    global tipo, menor, maior
    if tipo == 1:
        print("Apenas números diferentes são aceitos.")
    else:
        print("Os números em ordem crescente são:", menor, ",", maior)

def main():
    entrada()
    processamento()
    saida()

main()
