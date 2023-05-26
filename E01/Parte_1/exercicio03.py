brl = input("Insira o valo em reais para conversão: ")

def toUSD(brl):
    return brl / 5.32

usd = toUSD(brl)

print(f"O valor de {brl} reais para dolares é {usd}")