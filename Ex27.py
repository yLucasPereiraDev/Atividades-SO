voltas = int(input("Digite o número de voltas: "))
Ecirculo = float(input("Digite a extensão do circuito em metros: "))
tempo_duracao = float(input("Digite o tempo de duração em minutos: "))

distancia_total = (voltas * Ecirculo) / 1000
tempo_duracao = (tempo_duracao / 60)

velocidade_media = (distancia_total/tempo_duracao)

print(f"Velocidade média: {velocidade_media:.2f} km/h")
