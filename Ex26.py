n1: int = 0
n2: int = 0

n1 = int(input("Digite o primeiro valor: "))
n2 = int(input("Digite o segundo valor: "))

if (n1 > n2 and n1 % n2 == 0) or (n2 > n1 and n2 % n1 == 0):
    print("O valor maior é multiplo do menor! ")
else:
    print("O valor maior não é multiplo do menor! ")
