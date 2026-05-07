n1 = 0 
n2 = 0

def entrada():
    global n1, n2
    n1 = int(input("Digite o valor do primeiro número: "))
    n2 = int(input("Digite o valor do segundo número: "))

def processamento():
    global n1, n2, dif
    if n1 > n2:
        dif = (n1-n2)
    else:
        dif = (n2-n1)

def saida():
    global dif
    print("A diferença do maior número para o menor é de:", dif)

def main():
    entrada()
    processamento()
    saida()

main()
