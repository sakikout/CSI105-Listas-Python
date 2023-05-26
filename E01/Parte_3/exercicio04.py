print("Insira 10 valores: ")
array = []

i = 0
while ( i < 10):
    array.append(input(f"Valor {i + 1}: "))
    i += 1


def calcParOuImpar(array):
    i = 0
    pares = 0
    impares = 0
    while (i < len(array)):
        if (float(array[i]) % 2 == 0):
            pares += 1
        else:
            impares += 1
        i += 1
    return pares, impares

total = calcParOuImpar(array)
print(f"Total de numeros pares: {total[0]}\nTotal de numeros impares: {total[1]}")