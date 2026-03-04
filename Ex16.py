#Declaração de Variáveis
horasT: int = 0
valorH: float = 0
desconto: float = 0
ndescentendes: int = 0

#Início
horasT = int(input("Digite a quantidade de horas trabalhadas: "))
valorH = float(input("Digite o valor por hora trabalhada: "))
desconto = float(input("Digite o percentual de desconto: "))
ndescentendes = int(input("Digite a quantidade de descendentes: "))


salarioB = (horasT * valorH)
valorDesconto = (salarioB * (desconto / 100))
salarioL = (salarioB - valorDesconto)
salarioL = (salarioL + (ndescentendes * 100))

print (f"Seu salário líquido é: {salarioL:.2f}")
#Fim
