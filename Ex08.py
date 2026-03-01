#Declaração de Variáveis
Deposito: float = 0
Rentabilidade: float = 0

#Início
print("Poupança: rentabilidade -> 1,3 a.m.")
Deposito = float(input("Digite o valor do depósito: "))
Rentabilidade = (Deposito * 0.013)

Deposito = (Deposito + Rentabilidade)
print(f"O saldo da sua poupança com o reajuste de rentabilidade mensal é: {Deposito:.1f}") #Testando o f-strings para reduzir a quantidade de números após a vírgula
#Fim