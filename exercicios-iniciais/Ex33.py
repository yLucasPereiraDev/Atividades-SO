num = int(input("Digite um número: "))
d = 1
soma = 0


while d <= num:
    soma += (1/d)
    d += 1

print(f"Resultado da série: {soma:.3f}")