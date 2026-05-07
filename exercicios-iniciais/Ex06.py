#Declaração de Variáveis
X: int = 0
Y: int = 0

#Início
print ("Troca de Valores")
X = int(input("Digite o valor de X: "))
Y = int(input("Digite o valor de Y: "))

X, Y = Y, X
print("O valor de X é: ", X)
print("O valor de Y é: ", Y)
#Fim