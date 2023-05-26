tamanho = int(input("Insira o tamanho do triângulo: "))

def imprimir_triangulo(n):
    for i in range(1, n+1):
        print('* ' * i)


imprimir_triangulo(tamanho)
