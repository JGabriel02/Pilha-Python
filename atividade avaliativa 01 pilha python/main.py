from carro import Carro
from drone import Drone
from pilha import Pilha

def menu():


    while True:
        print("== MENU ==")
        print("1. Adicionar e imprimir Carros")
        print("2. Remover e imprimir Carros")
        print("3. Adicionar e imprimir Drones")
        print("4. Remover e imprimir Drones")
        print("0. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            c1 = Carro("FIAT","UNO", 4)
            c2 = Carro("Nissa","GTR", 2)
            c3 = Carro("Subaru","Empresa", 2)
            pilhacarros = Pilha()
            pilhacarros.add(c1)
            pilhacarros.add(c2)
            pilhacarros.add(c3)
        if escolha == "2":
            pilhacarros.remover()
            pilhacarros.remover()
            pilhacarros.remover()

        if escolha == "3":
            d1 = Drone("DJI "," Mini 3 Pro", 4)
            d2 = Carro("Autel","Drone Evo Lite+", 5)
            d3 = Carro("DJI ","Mini 3", 3)
            pilhadrones = Pilha()
            pilhadrones.add(d1)
            pilhadrones.add(d2)
            pilhadrones.add(d3)

        if escolha == "4":
            pilhadrones.remover()
            pilhadrones.remover()
            pilhadrones.remover()

        if escolha == "0":
            exit()




if __name__ == "__main__":
    menu()











