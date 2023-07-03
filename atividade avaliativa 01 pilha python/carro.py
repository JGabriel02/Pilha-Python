from veiculo import Veiculo

class Carro(Veiculo):
    def __init__(self, marca, modelo, portas):
        super().__init__(marca, modelo)
        self.__portas = portas
        self.proximo = None

    def __str__(self):
        texto = "Marca: " + self.marca
        texto += "\nModelo: " + self.modelo
        texto += "\nPortas: " + str(self.__portas)
        return texto
