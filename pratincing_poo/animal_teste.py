"Uma classe seria um tipo de molde pre pronto para facilitar a manipulacao de dados ou a criacao de situacoes, aonde nao iremos precisar repetir codigo"
"Podemos dizer que a classe é um molde aonde podemos definir os comportamentos de um objeto."
"Com isso, o codigo podera performar melhor e ter menos gastos"
class Animal():
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def miar(self):
        print("Miau")

animal1 = Animal("Frajola", 4)
print("Idade do animal: ", animal1.idade)
animal1.miar()
