vetor = []
soma_intervalo = 0
contador_intervalo = 0
soma_impares = 0

for i in range(50):
    num = int(input(f"Digite o {i+1}º número: "))
    vetor.append(num)

    #valores entre 10 e 200
    if 10 <= num <= 200:
        soma_intervalo += num
        contador_intervalo += 1

    #soma dos ímpares
    if num % 2 != 0:
        soma_impares += num
 
if contador_intervalo > 0:
    media = soma_intervalo / contador_intervalo
else:
    media = 0

print("Média dos números entre 10 e 200:", media)
print("Soma dos ímpares:", soma_impares)