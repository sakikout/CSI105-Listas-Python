
def calcPotencia(base, expoente):
    base = float(base)
    expoente = float(expoente)
    vezes = expoente
    resultado = 0

    while (vezes != 0):
       resultado += base * base
       vezes -= 2
    
    return resultado

numero = input("Insira o numero para o calculo da potencia: ")
expoente = input("Insira o valor do expoente: ")

resultado = calcPotencia(numero, expoente)

print(f"O resultado da potenciação é: {resultado}")
