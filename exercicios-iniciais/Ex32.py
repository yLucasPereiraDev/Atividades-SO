print("Cálculo de Fatorial")
num = int(input("Digite um número inteiro: "))
r = num
fat = 1

while num > 1:
    fat = (num*fat)
    num =  num - 1

print(r,"! =", fat)