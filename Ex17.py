#Declaração de Variáveis
tempo: float = 0
velocidadeM: float = 0

#Início
tempo = float(input("Digite o tempo do percurso: "))
velocidadeM = float(input("Digite a velocidade média: "))

print("O carro faz 12km/l")
distancia = (tempo * velocidadeM)
litros = (distancia / 12)

print(f"Distância percorrida: {distancia:.2f} km")
print(f"Litros gastos: {litros:.2f} litros")
#Fim