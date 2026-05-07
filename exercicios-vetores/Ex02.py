vetor = []
soma = 0

for i in range(100):
    num = int(input(f"Digite o {i+1}º número: "))
    vetor.append(num)
    soma += num

maior = max(vetor)
menor = min(vetor)
media = soma / 100

print("Maior valor:", maior)
print("Menor valor:", menor)
print("Média:", media)