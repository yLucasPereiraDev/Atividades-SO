tipo = int(input("Digite o tipo de investimento (1 = poupança, 2 = renda fixa): "))
valor = float(input("Digite o valor do investimento: "))

if tipo == 1:
    rendimento = valor * 0.03
    valor_corrigido = valor + rendimento
elif tipo == 2:
    rendimento = valor * 0.05
    valor_corrigido = valor + rendimento
else:
    print("Tipo de investimento inválido")
    valor_corrigido = 0

if valor_corrigido > 0:
    print("Valor corrigido em 30 dias: ", valor_corrigido)