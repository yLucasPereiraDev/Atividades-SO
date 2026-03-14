nota1 = float(input("Digite a nota do primeito bimestre do aluno: "))
nota2 = float(input("Digite a nota do segundo bimestre do aluno: "))
nota3 = float(input("Digite a nota do terceiro bimestre do aluno: "))
nota4 = float(input("Digite a nota do quarto bimestre do aluno: "))

media = ((nota1+nota2+nota3+nota4)/4)

print("A média aritmética das notas bimestrais do aluno é igual a: ", media)

if media >= 6:
    print("APROVADO")
elif media >= 3 and media <= 6:
    print("EXAME")
else:
    print("RETIDO")