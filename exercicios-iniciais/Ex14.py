#Declaração de Variáveis
a1: int = 0
a2: int = 0
a3: int = 0

#Início
a1 = int(input("Digite o valor do primeiro ângulo: "))
a2 = int(input("Digite o valor do segundo ângulo: "))

a3 = (180 - (a1+a2))

print("O valor do terceiro ângulo é: ", a3, "graus")
#Fim