tamanhoArquivo = input("Insira o tamanho do arquivo: ")
velocidade = input("Insira a velocidade da internet (Mbps): ")

tempoMinutos = (tamanhoArquivo / velocidade) / 60

print(f"O tempo aproximado de download em minutos é: {tempoMinutos}")