
dias = input("Numero de dias: ")
horas = input("Numero de horas: ")
minutos = input("Numero de minutos: ")

def converterDias(dias):
    dias = int(dias)
    return dias * 24

def converterHoras(horas):
    horas = int(horas)
    return horas * 60

def converterMinutos(minutos):
    minutos = int(minutos)
    return minutos * 60

def minutosTotais(horas, dias, minutos):
    hrs = converterDias(dias) + int(horas)
    minutos_total = converterHoras(hrs) + int(minutos)
    return converterMinutos(minutos_total)

print(f"Os segundos totais são: {str(minutosTotais(horas, dias, minutos))}")