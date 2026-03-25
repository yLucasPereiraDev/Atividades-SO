import math
a = 0
b = 0
c = 0
x1 = 0
x2 = 0
delta = 0
tipo = 0

def entrada():
    global a, b, c
    a = float(input("Digite o coeficiente A: ")) 
    b = float(input("Digite o coeficiente B: ")) 
    c = float(input("Digite o coeficiente C: "))

def processamento():
    global a, b, c, delta, x1, x2, tipo
    if a == 0:
        tipo = 1 #erro
    else:
        delta = b**2 - 4*a*c
        
        if delta > 0:
            x1 = (-b + math.sqrt(delta)) / (2*a) 
            x2 = (-b - math.sqrt(delta)) / (2*a)
            tipo = 2 #duas raízes
        elif delta == 0:
            x1 = -b/(2*a)
            tipo = 3 #uma raíz
        else:
            tipo = 4 #nenhuma
        
    
def saida():
    global delta, x1, x2, tipo
    if tipo == 1:
        print("O coeficiente A não pode ser zero em uma equação do 2º grau.")

    elif tipo == 2:
        print(f"Delta igual a: {delta:.1f}")
        print(f"Existem duas raízes reais: x1 = {x1:.1f} e x2 = {x2:.1f}")

    elif tipo == 3:
        print(f"Delta igual a: {delta:.1f}")
        print(f"Existe uma única raiz real: x = {x1:.1f}")

    elif tipo == 4:
        print(f"Delta igual a: {delta:.1f}")
        print("A equação não possui raízes reais.")

def main():
    entrada()
    processamento()
    saida()

main()