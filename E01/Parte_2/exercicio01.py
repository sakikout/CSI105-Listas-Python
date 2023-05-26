def calcIMC(peso, altura):
    return float(peso) / float((float(altura) * float(altura)))


peso = input("Insira seu peso (em quilos): ")
altura = input("Insira sua altura (em metros): ")
imc = calcIMC(peso, altura)

if (imc >= 18.5 and imc <= 25.0):
    print("Seu IMC é %.2f, classificado como Peso Normal." % imc)
elif (imc > 25.0):
    print("Seu IMC é %.2f, classificado como Sobrepeso." % imc)
elif (imc < 18.5):
    print("Seu IMC é %.2f, classificado como Abaixo do Peso." % imc)