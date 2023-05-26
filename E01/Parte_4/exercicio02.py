
def retirarNegativos(array):
    lista = []
    for item in array:
        if (float(item) > 0):
           lista.append(item) 
        
    return lista

def mostrarLista(lista):
    for item in lista:
        print(item)

print("Insira 10 valores para a lista: ")
lista = []
i = 0
while( i < 10):
    lista.append(input(f"Valor {i + 1}: "))
    i += 1

lista_positiva = retirarNegativos(lista)
print("\nNova lista apenas com valores positivos:")
mostrarLista(lista_positiva)
