from funcionario import Funcionario

print("Informe os seguintes campos para o calculo")
nome = input("Nome: ")
salHora = input("Salario por hora: ")
hrsMes = input("Horas trabalhadas: ")

funcionario = Funcionario(salHora, hrsMes, nome)

funcionario.mostrarDados()