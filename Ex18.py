n1: int = 0
n2: int = 0


n1 = int(input("Digite o valor do primeiro número: "))
n2 = int(input("Digite o valor do segundo número: "))

if (n1 > n2):
    dif = (n1 - n2)
else:
    dif = (n2 - n1)

print("A diferença do maior número para o menor é de: " , dif)
