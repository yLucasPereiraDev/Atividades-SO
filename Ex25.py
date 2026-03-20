h1 = int(input("Digite a hora inicial: "))
m1 = int(input("Digite os minutos iniciais: "))

h2 = int(input("Digite a hora final: "))
m2 = int(input("Digite os minutos finais: "))

inicio = (h1 * 60 + m1)
fim = (h2 * 60 + m2)

if (fim < inicio):
    fim = (fim + 24 * 60)

duracao = fim - inicio

horas = duracao // 60
minutos = duracao % 60

print(f"O jogo durou {horas} horas e {minutos} minutos")