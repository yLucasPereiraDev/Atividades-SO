import math

A = float(input("Digite o coeficiente A: "))
B = float(input("Digite o coeficiente B: "))
C = float(input("Digite o coeficiente C: "))

if A == 0:
    print("O coeficiente A não pode ser zero em uma equação do 2º grau.")
else:
    delta = B**2 - 4*A*C
    print(f"Delta igual a: {delta:.1f}")

    if delta > 0:
        X1 = (-B + math.sqrt(delta)) / (2*A)
        X2 = (-B - math.sqrt(delta)) / (2*A)
        print(f"Existem duas raízes reais: x1 = {X1:.1f} e x2 = {X2:.1f}")
    
    elif delta == 0:
        X = -B / (2*A)
        print(f"Existe uma única raiz real: x = {X:.1f}")
    
    else:
        print("A equação não possui raízes reais.")