n1 = int(input("Digite o valor do primeiro número: "))
n2 = int(input("Digite o valor do segundo número: "))

if n1 == n2:
    print("Apenas números diferentes são aceitos.")
elif (n1 > n2):
    print("Os números em ordem crescente são: ", n2, ",", n1)
else:
    print("Os números em ordem crescente são: ", n1, ",", n2)
