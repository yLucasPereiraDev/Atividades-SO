import math

#Declaração de Variáveis
c1: int = 0
c2: int = 0
h: float = 0

#Início
c1 = int(input("Digite o valor do primeiro cateto: "))
c2 = int(input("Digite o valor do segundo cateto: "))

h = math.sqrt((c1**2) + (c2**2))

print(f"O valor da hipotenusa é igual {h:.1f}")
#Fim