class Carro:
    def __init__(self, consumo, quantidade) -> None:
        self.consumo = 0
        self.quantidade_tanque = 0
        try:
            self.consumo = float(consumo)
            self.quantidade_tanque = float(quantidade)
        except ValueError as e:
            print("Erro no formato do parâmetro informado.\n")

    def andar(self, dist):
        combustivel = float(dist) / self.consumo
        self.quantidade_tanque = self.quantidade_tanque - combustivel
        if (self.quantidade_tanque < 0):
            self.quantidade_tanque = 0
        
        print(f"Dirigir {dist}km consumiu {combustivel}L de combustível.")
        print(f"Combustível disponível: {self.quantidade_tanque}\n")

    def abastecer(self, qtde):
        try:
            self.quantidade_tanque += float(qtde)
        except ValueError as e:
            print("Insira um parâmetro em formato numérico.\n")

    def mostrar_tanque(self):
        print(f"Combustível disponível: {self.quantidade_tanque}\n")