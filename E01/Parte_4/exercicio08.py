def MDC(num1, num2):
    if int(num2) == 0:
        return int(num1)
    else:
        return MDC(int(num2), int(num1) % int(num2))

numero1 = input("Insira o primeiro numero: ")
numero2 = input("Insira o segundo numero: ")

print(f"O MDC entre o numero {numero1} e numero {numero2} é: {MDC(numero1, numero2)}")