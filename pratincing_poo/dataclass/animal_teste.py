from dataclasses import dataclass

@dataclass
class Animal:
    nome: str
    idade: int
    raca: str

    def miar(self):
        print("miau")


animal1 = Animal(nome="Frajola", idade= 4, raca="Gato")
print(f"nome do animal: {animal1.nome}. Idade do animal {animal1.idade}. A raca do animal é: {animal1.raca}")
animal1.miar()


# class Animal():
#     def __init__(self, nome, idade):
#         self.nome = nome
#         self.idade = idade

#     def miar(self):
#         print("Miau")

# animal1 = Animal("Frajola", 4)
# print("Idade do animal: ", animal1.idade)
# animal1.miar()
