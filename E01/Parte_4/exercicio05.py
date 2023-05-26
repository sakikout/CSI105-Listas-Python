
def checarOcorrencia(string, char):
    ocorrencias = 0
    for c in string:
        if (c == char):
            ocorrencias += 1

    return ocorrencias

palavra = input("Insira uma palavra: ")
caractere = input("Insira o caractere para pesquisar: ")
ocorrencias = checarOcorrencia(palavra, caractere)

print(f"O caractere {caractere} aparece {ocorrencias} vezes na string {palavra}")