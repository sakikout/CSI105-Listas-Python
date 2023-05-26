def inverterString(string):
    return string[::-1]

def checarPalindromo(string):
    invertida = inverterString(string)

    if (invertida == string):
        return True
    
    return False


palavra = input("Insira uma string para checagem: ")

resultado = checarPalindromo(palavra)

if(resultado == True):
    print(f"A palavra {palavra} é um palíndromo")
else:
    print(f"A palavra {palavra} não é um palíndromo")