
numero = input("Insira um numero: ")

def verificarPrimo(num):
    tam = float(num) / 2
    tam = int(tam)
    flag = 0

    if (float(num) % 2 == 0):
        return False

    while (tam > 0):
        if (float(num) % tam == 0):
            flag += 1
        tam = tam - 2
    if (flag == 0 or flag == 1):
        return True
    
    return False

def verificarDivisores(num):
    tam = float(num) / 2
    tam = int(tam)
    arr = []
    arr.append(float(num))

    if (float(num) % 2 == 0):
        return False

    while (tam > 0):
        if (float(num) % tam == 0):
            arr.append(tam)
        tam = tam - 2
    return arr

verificacao = verificarPrimo(numero)
arr = verificarDivisores(numero)

if (verificacao):
    print(f"O numero {numero} é primo.")
else:
    print(f"O numero {numero} não é primo e é divisível pelos números: {arr}")
    