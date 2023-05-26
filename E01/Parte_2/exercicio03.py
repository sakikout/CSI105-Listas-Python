
def calc_alcool_desconto(litros):
    litros = float(litros)
    preco = 2.80
    if (litros <= 20):
        total = litros * (preco * 0.97)
    elif (litros > 20):
        total = litros * (preco * 0.95)
    return total

def calc_gasolina_desconto(litros):
    litros = float(litros)
    preco = 4.20
    if (litros <= 20):
        total = litros * (preco * 0.96)
    elif (litros > 20):
        total = litros * (preco * 0.94)
    return total

def calc_alcool(litros):
    litros = float(litros)
    preco = 2.80
    total = litros * (preco)
   
    return total

def calc_gasolina(litros):
    litros = float(litros)
    preco = 4.20
    total = litros * (preco)
    
    return total

print("COMBUSTIVEIS\nG - Gasolina\nA - Alcool")
print(f"Gasolina:\nate 20L, 4% desconto por litro\nacima de 20L, 6% desconto por litro")
print(f"Alcool:\nate 20L, 3% desconto por litro\nacima de 20L, 5% desconto por litro\n")


flag = True

while(flag):
    litros = input("Insira o numero de litros vendidos: ")
    tipo = input("Insira o tipo de combustivel: ")

    tipo = tipo.upper()

    if (tipo == 'A'):
        total = calc_alcool_desconto(litros)
        total_sem = calc_alcool(litros)
        flag = False
    elif (tipo == 'G'):
        total = calc_gasolina_desconto(litros)
        total_sem = calc_gasolina(litros)
        flag = False
    else:
        print("Invalido.")

print("\nTotal sem desconto: R$%.2f" % total_sem)
print("Total com desconto: R$%.2f" % total)
    