
print("Insira 5 valores: ")
checagem = []

i = 0
while ( i < 5):
    checagem.append(input(f"Valor {i + 1}: "))
    i += 1

def encontrarMax(numeros):
    array = numeros
    i = 0
    maxNum = float(array[i])
    while (i < len(array)):
        if (maxNum < float(array[i])):
            maxNum = float(array[i])
            maxPos = i + 1
        
        i += 1
    return maxNum, maxPos

maxNum = encontrarMax(checagem)

print(f"O maior é numero o {maxNum[1]}º valor: {maxNum[0]}")