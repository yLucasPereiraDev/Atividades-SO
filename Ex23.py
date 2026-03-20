n1 = int(input("Digite o valor do primeiro número: "))
n2 = int(input("Digite o valor do segundo número: "))
n3 = int(input("Digite o valor do terceiro número: "))
n4 = int(input("Digite o valor do quarto número: "))

if (n4 < n1):
    print(n4, ",", n1, ",", n2,",", n3)
elif (n4 < n2):
    print(n1, ",", n4, ",", n2,",", n3)
elif (n4 < n3):
    print(n1, ",", n2,",",n4, "," ,n3)   
else:
    print(n1, ",", n2,",", n3, ",", n4)

