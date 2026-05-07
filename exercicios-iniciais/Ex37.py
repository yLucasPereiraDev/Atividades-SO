num = int(input("Digite a quantidade de termos: "))

a = 0
b = 1

print("Sequência de Fibonacci:")

for i in range(num):
    print(a)
    proximo = a + b
    a = b
    b = proximo