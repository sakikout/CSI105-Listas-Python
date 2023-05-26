grausF = input("Insira a temperatura em graus Fahrenheit: ")

def toCelsius(fahrenheit):
    return 5 * ((fahrenheit - 32) / 9)

grausC = toCelsius(grausF)

print(f"A temperatura {grausF} em graus Fahrenheit para graus Celsius é {grausC}")