h1 = 0
m1 = 0
h2 = 0
m2 = 0
dur_h = 0
dur_m = 0

def entrada():
    global h1, m1, h2, m2
    h1 = int(input("Hora inicial: "))
    m1 = int(input("Minuto inicial: "))
    h2 = int(input("Hora final: "))
    m2 = int(input("Minuto final: "))

def processamento():
    global h1, m1, h2, m2, dur_h, dur_m

    inicio = h1 * 60 + m1
    fim = h2 * 60 + m2

    if fim < inicio:
        fim += 24 * 60

    duracao = fim - inicio

    dur_h = duracao // 60
    dur_m = duracao % 60

def saida():
    global dur_h, dur_m
    print(f"Duração do jogo: {dur_h} horas e {dur_m} minutos")

def main():
    entrada()
    processamento()
    saida()

main()