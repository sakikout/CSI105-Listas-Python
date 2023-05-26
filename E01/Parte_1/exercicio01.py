def area (raio):
    try:
        a = 3.14 * raio * raio
    except ValueError as e:
        print("Formato invalido para o calculo da área.")
        return e
    return a

def perimetro(raio):
    try:
        p = 2 * 3.14 * raio
    except ValueError as e:
        print("Formato invalido para o calculo do perímetro.")
        return e
    return p

print("CALCULO DA AREA E PERIMETRO (CÍRCULO)")
raio = input("Raio (em cm): ")
raio = float(raio)
area = area(raio)
perimetro = perimetro(raio)

print("A area do circulo é %.2f" %area + " e seu perimetro é %.2f" %perimetro)