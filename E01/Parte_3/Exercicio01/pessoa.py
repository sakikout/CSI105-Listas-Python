class Pessoa:
      
    def setNome (self, nome):
        self.nome = nome   

    def setIdade (self, idade):
        self.idade = int(idade)

    def setSalario (self, salario):
        self.salario = float(salario)
    
    def setSexo (self, sexo):
       self.sexo = sexo.upper()
    
    def setEstado (self, estado):
        self.estado = estado.upper()

    def checarDados(self):
        nome = 1
        sexo = 1
        estado = 1
        salario = 1
        idade = 1

        if (len(self.nome) < 3):
            nome = 0
        if (self.sexo != 'F'):
            if(self.sexo != 'M'):
                sexo = 0
           
        if (self.estado != 'S'):
            if(self.estado != 'C'):
                if (self.estado != 'V'):
                    if(self.estado != 'D'):
                        estado = 0
        if (self.salario <= 0):
            salario = 0
        if (self.idade > 150 or self.idade < 0):
            idade = 0

        return nome, sexo, estado, salario, idade
    
    def mostrarDados(self):
        print("-------------------DADOS------------------")
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade}")
        print(f"Sexo: {self.sexo}")
        print(f"Estado Civil: {self.estado}")
        print(f"Salario: {self.salario}")