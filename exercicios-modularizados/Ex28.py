def entrada():
    ptproduto = float(input("Digite o preço atual do produto: ")) 
    vendamensal = int(input("Digite a média mensal de venda do produto: "))
    return ptproduto, vendamensal

def processamento(ptproduto, vendamensal):
    if (vendamensal < 500) and (ptproduto < 30): 
        pnproduto = ((ptproduto/100) * 10) + ptproduto
        tipo = 1 #10%
    elif (vendamensal >= 500 and vendamensal < 1000) and (ptproduto >= 30 and ptproduto < 80): 
        pnproduto = ((ptproduto/100) * 15) + ptproduto
        tipo = 2 #15%
    elif (vendamensal >= 1000) and (ptproduto >= 80): 
        pnproduto = ((ptproduto/100) * - 5) + ptproduto
        tipo = 3 #-5%
    else: 
        pnproduto = ptproduto
        tipo = 4 #Condição não listada
    return pnproduto, tipo

def saida(ptproduto, pnproduto, tipo):
    if tipo == 1:
        print(f"Novo preço: {pnproduto: .2f}")
    elif tipo == 2: 
        print(f"Novo preço: {pnproduto: .2f}")
    elif tipo == 3:
        print(f"Novo preço: {pnproduto: .2f}")
    else:
        print(f"Condição não listada, preço sem alterações: {ptproduto: .2f}")

def main():
    ptproduto, vendamensal = entrada()
    pnproduto, tipo = processamento(ptproduto, vendamensal)
    saida(ptproduto, pnproduto, tipo)

main()