ptproduto: float = 0
pnproduto: float = 0
vendamensal: int = 0

ptproduto = float(input("Digite o preço atual do produto: "))
vendamensal = int(input("Digite a média mensal de venda do produto: "))

if (vendamensal < 500) and (ptproduto < 30):
    pnproduto = ((ptproduto/100) * 10) + ptproduto
    print(f"Novo preço: {pnproduto: .2f}")
elif (vendamensal >= 500 and vendamensal < 1000) and (ptproduto >= 30 and ptproduto < 80):
    pnproduto = ((ptproduto/100) * 15) + ptproduto
    print(f"Novo preço: {pnproduto: .2f}")
elif (vendamensal >= 1000) and (ptproduto >= 80):
    pnproduto = ((ptproduto/100) * - 5) + ptproduto
    print(f"Novo preço: {pnproduto: .2f}")
else:
    print(f"Condição não listada, preço sem alterações: {ptproduto: .2f}")
    