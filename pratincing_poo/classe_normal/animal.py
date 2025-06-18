class Animal:
    def __init__(self, cor, raca, idade):
        self.cor = cor
        self.raca = raca
        self.idade = idade

    def fazer_som(self):
        print("Som do animal")


class Gato(Animal):
    def __init__(self, cor, raca, idade):
        super().__init__(cor, raca, idade)

    def fazer_som(self):
        print("Miau")



class Cachorro(Animal):
    def __init__(self, cor, raca, idade):
        super().__init__(cor, raca, idade)

    def fazer_som(self):
        print("Au Au")


class Passaro(Animal):
    def __init__(self, cor, raca, idade):
        super().__init__(cor, raca, idade)

    def fazer_som(self):
        print("Som de passaro")

g = Gato("Cinza", "Siamês", 3)
c = Cachorro("Marrom", "Labrador", 5)

g.fazer_som()  
c.fazer_som()  
