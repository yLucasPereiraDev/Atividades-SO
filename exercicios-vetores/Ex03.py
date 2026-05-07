vetor = []
soma = 0

for i in range(30):
    num = float(input(f"Digite o {i+1}º número: "))
    vetor.append(num)
    soma += num

media = soma / 30

#quantidade acima da média
acima_media = 0

#posições abaixo da média
posicoes_abaixo = []

for i in range(30):
    if vetor[i] > media:
        acima_media += 1
    elif vetor[i] < media:
        posicoes_abaixo.append(i)

print("Média:", media)
print("Quantidade acima da média:", acima_media)
print("Posições abaixo da média:", posicoes_abaixo)