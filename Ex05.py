import math

#Declaração de Variáveis
A = float(input("Digite A: "))
B = float(input("Digite B: "))
C = float(input("Digite C: "))

#Início
delta = B**2 - 4*A*C

if delta > 0:
    x1 = (-B + math.sqrt(delta)) / (2*A)
    x2 = (-B - math.sqrt(delta)) / (2*A)
    print (f"Duas raízes reais diferentes: {x1:.2f} e {x2:.2f}")

elif delta == 0:
    x = -B / (2*A)
    print (f"Raiz real única: {x:.2f}")

else:
    print ("Não possui raízes reais.")
#Fim