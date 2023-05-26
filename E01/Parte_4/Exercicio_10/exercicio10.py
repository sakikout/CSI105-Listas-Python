from carro import Carro

def Menu():
    flag = True
    while(flag):  
        resposta = input("Deseja andar com o carro? S - Sim ou N - Não\n")
        resposta = resposta.upper()

        if(resposta == 'S'):
            kms = input("Insira a distância em quilometros (km) para percorrer:\n")
            carro.andar(kms)
        elif (resposta == 'N'):
            resp_abastecer = input("Deseja abastecer o carro? S - Sim ou N - Não\n")
            resp_abastecer = resp_abastecer.upper()
            if (resp_abastecer == 'S'):
                qtde = input("Insira a quantidade em litros (L) para abastecer:\n")
                carro.abastecer(qtde)
            elif(resp_abastecer == 'N'):
                flag = False
    return

print("Insira os dados do carro: ")
combustivel = input("Consumo de combustível (km/l): ")
quantidade = input("Quantidade disponível no tanque: ")

carro = Carro(combustivel, quantidade)

Menu()

carro.mostrar_tanque()
