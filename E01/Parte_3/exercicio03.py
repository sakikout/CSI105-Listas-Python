
print("Insira 5 valores: ")
array = []

i = 0
while ( i < 5):
    array.append(input(f"Valor {i + 1}: "))
    i += 1

def media_e_soma(numeros):
    array = numeros
    i = 0
    soma = 0
    while (i < len(array)):
        soma += float(array[i])
        i += 1
    media = soma / len(array)
    return soma, media

resultado = media_e_soma(array)

print(f"Media dos valores: {resultado[1]}\nSoma dos valores: {resultado[0]}")