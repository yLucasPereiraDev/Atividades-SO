def entrada():
    tipo = int(input("Digite o tipo de investimento (1 = poupança, 2 = renda fixa): "))
    valor = float(input("Digite o valor do investimento: "))
    return tipo, valor

def processamento(tipo, valor):
    if tipo == 1:
        rendimento = valor * 0.03
        valor_corrigido = valor + rendimento
        status = 1

    elif tipo == 2:
        rendimento = valor * 0.05
        valor_corrigido = valor + rendimento
        status = 2

    else:
        valor_corrigido = 0
        status = 3  # inválido

    return valor_corrigido, status

def saida(valor_corrigido, status):
    if status == 1:
        print(f"Poupança → Valor corrigido em 30 dias: {valor_corrigido:.2f}")

    elif status == 2:
        print(f"Renda fixa → Valor corrigido em 30 dias: {valor_corrigido:.2f}")

    else:
        print("Tipo de investimento inválido!")

def main():
    tipo, valor = entrada()
    valor_corrigido, status = processamento(tipo, valor)
    saida(valor_corrigido, status)

main()