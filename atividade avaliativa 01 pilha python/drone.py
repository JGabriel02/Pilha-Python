from veiculo import Veiculo

class Drone(Veiculo):
    def __init__(self, marca, modelo, quantidade_helices):
        super().__init__(marca, modelo)
        self._quantidade_helices = quantidade_helices
        self.proximo = None

    def __str__(self):
        texto = "Marca: " + self.marca
        texto += "\nModelo: " + self.modelo
        texto += "\nQuantidade de helices: " + str(self._quantidade_helices)
        return texto
