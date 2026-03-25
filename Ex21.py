n1 = 0
n2 = 0
n3 = 0
n4 = 0
media = 0
tipo = 0

def entrada():
    global n1, n2, n3, n4
    n1= float(input("Digite a nota do primeito bimestre do aluno: ")) 
    n2= float(input("Digite a nota do segundo bimestre do aluno: ")) 
    n3 = float(input("Digite a nota do terceiro bimestre do aluno: ")) 
    n4 = float(input("Digite a nota do quarto bimestre do aluno: "))

def processamento():
    global n1, n2, n3, n4, media, tipo
    media = ((n1+n2+n3+n4)/4)

    if media >= 6:
        tipo = 1 #Aprovado
    elif media >= 3:
        tipo = 2 #Exame
    else: 
        tipo = 3 #Retido

def saida():
    global media, tipo
    print("A média aritmética das notas bimestrais do aluno é igual a: ", media)

    if tipo == 1:
        print("APROVADO")
    elif tipo == 2:
        print('EXAME')
    else:
        print('RETIDO')
    
def main():
    entrada()
    processamento()
    saida()

main()