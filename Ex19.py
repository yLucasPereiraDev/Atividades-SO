n1 = 0
n2 = 0
maior = 0

def entrada ():
    global n1, n2
    n1 = int(input("Digite o valor do primeiro número: "))
    n2 = int(input("Digite o valor do segundo número: "))

def processamento():
    global n1, n2, maior
    if n1 > n2:
        maior = (n1)
    else:
        maior = (n2)

def saida():
    global maior
    print("O valor do maior entre eles é: ", maior)

def main():
    entrada()
    processamento()
    saida()

main()
