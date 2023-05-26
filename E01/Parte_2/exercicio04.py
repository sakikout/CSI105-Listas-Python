
def calcNotas(total):
    saque = float(total)
    duzentos = 0
    cem = 0
    cinquenta = 0
    dez = 0

    while(saque - 200 >= 0):
        duzentos += 1
        saque = saque - 200
    
    while(saque - 100 >= 0):
        cem += 1
        saque = saque - 100
    
    while(saque - 50 >= 0):
        cinquenta += 1
        saque = saque - 50
   
    while(saque - 10 >= 0):
        dez += 1
        saque = saque - 10
    
    return [dez, cinquenta, cem, duzentos]

def mostrarNotas(notas):
    print("Serão entregues:")
    if (notas[0] != 0):
        print(f"{notas[0]} de 10 reais")
    if (notas[1] != 0):
        print(f"{notas[1]} de 50 reais")
    if (notas[2] != 0):
            print(f"{notas[2]} de 100 reais")
    if (notas[3] != 0):    
        print(f"{notas[3]} de 200 reais")
        

print("CAIXA ELETRONICO\nNotas disponíveis: 10, 50, 100 e 200 reais\n")

flag = True

while (flag):
    saque = input("Informe o valor para sacar (apenas multiplos de 10): ")
    
    if (float(saque) % 10 != 0):
        print("Apenas multiplos de 10 são permitidos para o saque.")
    else:
        flag = False

totalNotas = calcNotas(saque)
mostrarNotas(totalNotas)

    
