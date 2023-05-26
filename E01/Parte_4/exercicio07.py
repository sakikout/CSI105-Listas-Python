def vogais(string):
    string = string.lower()
    count = 0
    for v in string:
        if (v == 'a' or v == 'e' or v == 'i' or v == 'o' or v == 'u'):
            count += 1
        
    return count

palavra = input('Insira uma palavra: ')

print(f"O número de vogais na palavra {palavra} é: {vogais(palavra)}")
