tamanho = int(input("Insira o tamanho do quadrado: "))

def imprimir_quadrado(n):
    for i in range(n):
        for j in range(n):
            if i == 0 or i == n-1 or j == 0 or j == n-1:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()


imprimir_quadrado(tamanho)
