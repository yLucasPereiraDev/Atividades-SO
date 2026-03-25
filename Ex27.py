def entrada():
    voltas = int(input("Digite o número de voltas: "))
    ecirculo = float(input("Digite a extensão do circuito em metros: "))
    tempo = float(input("Digite o tempo de duração em minutos: "))
    return voltas, ecirculo, tempo

def processamento(voltas, ecirculo, tempo):
    distancia_total = (voltas * ecirculo) / 1000
    tempo_horas = tempo / 60
    velocidade_media = distancia_total / tempo_horas
    return velocidade_media

def saida(velocidade_media):
    print(f"Velocidade média: {velocidade_media:.2f} km/h")

def main():
    v, e, t = entrada()
    resultado = processamento(v, e, t)
    saida(resultado)

main()
