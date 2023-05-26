from pessoa import Pessoa

def criarPessoa(pessoa : Pessoa):
    print("Insira seus dados: ")
    pessoa.setNome(input("Nome: "))
    pessoa.setIdade(input("Idade: "))
    pessoa.setSexo(input("Sexo (M ou F): "))
    pessoa.setEstado(input("Estado Civil (S - Solteiro, C - Casado, V - Viuvo ou D - Divorciado): "))
    pessoa.setSalario(input("Salario: ")) 


def validar(pessoa: Pessoa): 
    i = 0
    flag = True

    while(flag):
        checagem = pessoa.checarDados()
        if ( checagem[0] == 0 ):
            pessoa.setNome(input("Nome invalido. Insira um nome válido: "))

        elif (checagem[1]== 0):
            pessoa.setSexo(input("Sexo invalido. Insira um sexo válido (M ou F): "))
        
        elif(checagem[2] == 0):
            pessoa.setEstado(input("Estado Civil invalido. Insira um estado civil válido (S - Solteiro, C - Casado, V - Viuvo ou D - Divorciado): "))

        elif(checagem[3] == 0):
            pessoa.setSalario(input("Salario inválido. Insira um salário válido: "))

        elif (checagem[4] == 0):
            pessoa.setIdade(input("Idade inválida. Insira uma idade válida: "))

        else:
            tam = 0
            while(i < len(checagem)):
                if (checagem[i] == 1):
                    tam += 1
                i += 1
            if (tam == 5):
                flag = False
   

pessoa = Pessoa()

criarPessoa(pessoa)
validar(pessoa)
pessoa.mostrarDados()