def calcImpostoRenda(salario):
    salario = float(salario)
    aliquota = 0
   
    if (salario <= 1904):
        return 0
    elif (salario > 1904 and salario <= 2826.65):
        aliquota = 0.075
        #deducao = 142.80
    elif (salario > 2826.65 and salario <= 3751.05 ):
        aliquota = 0.15
        #deducao = 354.80
    elif(salario > 3751.05 and salario <= 4664.68 ):
        aliquota = 0.225
        #deducao = 636.13
    elif (salario > 4664.68 ):
        aliquota = 0.275
        #deducao = 869.36

    impostoRenda = salario * aliquota
    return impostoRenda

print("CALCULO IMPOSTO DE RENDA")
salario = input("Salario: ")

impostoRenda = calcImpostoRenda(salario)

if(impostoRenda):
    print("O imposto de renda calculado é: %.2f" % impostoRenda)
else: 
    print("Houve a insenção do imposto de renda.")    