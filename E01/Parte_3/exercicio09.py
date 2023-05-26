
cA = [] # Notas entre 9 e 10
cB = [] # Notas entre 8 e 9
cC = [] # Notas entre 7 e 8
cD = [] # Notas entre 6 e 7
cE = [] # Notas entre 0 e 6

i= 0
flag = True
print("Insira as notas (de 0.0 a 10.0):\nDigite -1 para parar de adicionar.\n")

while(flag):
    nota = input(f"Nota {i + 1}: ")
    i += 1

    nota = float(nota)

    if (nota >= 9 and nota <= 10):
        cA.append(nota)
    elif(nota >= 8 and nota < 9):
        cB.append(nota)
    elif(nota >= 7 and nota < 8):
        cC.append(nota)
    elif(nota >= 6 and nota < 7):
        cD.append(nota)
    elif(nota < 6 and nota >= 0):
        cE.append(nota)
    elif (int(nota) == -1):
        flag = False

def printNotas(array, conceito):
    print(f"\nNotas no Conceito {conceito}: ")
    for item in array:
        print(item)

printNotas(cA, 'A')
printNotas(cB, 'B')
printNotas(cC, 'C')
printNotas(cD, 'D')
printNotas(cE, 'E')