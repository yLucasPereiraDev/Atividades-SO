#Declaração de Variáveis
AN: int = 0
AT: int = 0
IF: int = 0

#Início

AN = int(input("Digite seu ano de nascimento: "))
AT = int(input("Digite o ano atual: "))

IF = ((AT-AN) + 17)

print ("Daqui a 17 anos você terá: ", IF)
#Fim