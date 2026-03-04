import math

#Declaração de Variáveis
Raio: float = 0
Comprimento: float = 0

#Início
print ("Considererando pi igual: ")
print (math.pi)

Raio = float(input("Digite o valor do raio da circunferência: "))
Comprimento = (2 * math.pi * Raio)

print (f"O comprimento da circunferência é igual a: {Comprimento:.2f}")
#Fim