num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))

if num1 > num2:
    maiorn = num1
    menorn = num2
else:
    maiorn = num2
    menorn = num1

soma = 0

for i in range (menorn +1, maiorn):
    if i % 2 != 0:
        soma += i
print('Soma dos números ímpares: ', soma)