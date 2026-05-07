#Declaração de Variáveis
alimentoK: float = 0
gramaD: int = 50
consumo: float = 0

#Início
alimentoK = float(input("Digite a quantidade de alimento em Kilos: "))
alimentoK = (alimentoK * 1000)
consumo = (alimentoK / gramaD)

print(f"Ao consumir 50g ao dia, o tempo estimado que durará seu alimento é de: {consumo:.0f} dias")
#Fim