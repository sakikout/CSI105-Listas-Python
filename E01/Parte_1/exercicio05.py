tamanhoArea = input("Informe o tamanho da area a ser pintada em metros quadrados: ")

def calcularTotalTintas(area):
    areaDiv = area / 3
    totalLitros = 1
    totalTintas = 1

    while(areaDiv >= 1):
        totalLitros += 1
        areaDiv = areaDiv / 3
        
    while(totalLitros / 18 >= 1):
        totalTintas += 1
        totalLitros = totalLitros / 18

    precoTotal = totalTintas * 80

    return totalTintas, precoTotal

tintas = calcularTotalTintas(tamanhoArea)

print(f"O total de tintas a serem compradas é {tintas[0]}, custando R${tintas[1]}")