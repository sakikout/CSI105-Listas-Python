class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = float(salario)
        self.cargo = ''

    def setNome(self, nome):
        self.nome = nome

    def setSalario(self, salario):
        self.salario = float(salario)

    def setCargo(self, cargo):
        self.cargo = cargo

    def getCargo(self):
        return self.cargo

    def getNome(self):
        return self.nome

    def getSalario(self):
        return self.salario
    
    def mostrarDados(self):
        print("--------- DADOS DO FUNCIONARIO ------------")
        print(f"NOME: {self.nome}\nSALARIO: {self.salario}")
        if (self.cargo != ''):
            print(f"CARGO: {self.cargo}\n")
        
    def toString(self):
        if (self.cargo != ''):
           return "Nome do Funcionário é " + self.nome + ", do cargo de " + self.cargo +", com salário de " + str(self.salario) + " reais." 
        return "Nome do Funcionário é " + self.nome + ", com salário de " + str(self.salario) + " reais."