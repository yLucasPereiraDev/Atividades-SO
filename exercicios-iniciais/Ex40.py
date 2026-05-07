num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

for i in range(num1 +1, num2):
    if i > 1 :
        primo = True

        for j in range(2, i):
            if i % j == 0:
                primo = False
                break
        if primo:
            print(i)