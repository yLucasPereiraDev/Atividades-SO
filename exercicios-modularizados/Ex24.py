num = 0
tipo = 0

def entrada():
    global num
    num = int(input("Digite um número: "))

def processamento():
    global num, tipo
    if num % 2 == 0 and num % 3 == 0:
        tipo = 1
    else:
        tipo = 2

def saida():
    global tipo
    if tipo == 1:
        print("É divisível por 2 e por 3.")
    else:
        print("Não é divisível por 2 e por 3.")

def main():
    entrada()
    processamento()
    saida()

main()



