from funcionario import Funcionario

print("Insira os dados do funcionário: ")
nome = input("Nome: ")
salario = input("Salario: ")

funcionario = Funcionario(nome, salario)

print("Inserir cargo? S - Sim ou N - Não ")
resposta = input("Resposta: ")

resposta = resposta.upper()
if( resposta == 'S'):
    funcionario.setCargo(input("Insira o cargo: "))
elif ( resposta == 'N'):
    print("Cargo não informado.")
else:
    print("Resposta inválida.")

funcionario.mostrarDados()