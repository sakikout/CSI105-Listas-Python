class Funcionario:
    def __init__(self, salHora, hrsMes, nome):
        self.nome = nome
        try:
            self.salHora = float(salHora)
            self.hrsMes = float(hrsMes)
            self.salarioBruto = float(salHora) * float(hrsMes)
        except ValueError as e:
            print("Formato inválido para o cálculo.")
            print(e)

        self.impostoRenda = self.calcImpostoRenda()
        self.inss = self.calcINSS()
        self.sindicato = self.calcSindicato()
        self.salarioLiquido = self.calcSalarioLiq()

    def calcImpostoRenda(self):
        return self.salarioBruto * 0.12
    
    def calcINSS(self):
        return self.salarioBruto * 0.10
    
    def calcSindicato(self):
        return self.salarioBruto * 0.02
    
    def calcSalarioLiq(self):
        return self.salarioBruto - (self.sindicato + self.inss + self.impostoRenda)
    
    def mostrarDados(self):
        print(f"--------------- Funcionario {self.nome} ------------------")
        print(f"Salario Bruto: {self.salarioBruto}\nSalario Liquido: {self.salarioLiquido}")
        print("Imposto de Renda: %.2f" % self.impostoRenda)
        print("INSS: %.2f" % self.inss)
        print("Sindicato: %.2f" % self.sindicato)