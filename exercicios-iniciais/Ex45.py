soma = 0

for i in range(1, 16):
    termo = i / (i * i)
    
    if i % 2 == 0:
        soma -= termo
    else:
        soma += termo

print("Resultado da série:", soma)