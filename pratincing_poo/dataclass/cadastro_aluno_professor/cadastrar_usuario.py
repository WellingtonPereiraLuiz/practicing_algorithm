from dataclasses import dataclass

@dataclass
class Pessoas:
    nome:str
    idade:int
    
    def apresentar(self):
        print(f"O nome é {self.nome} e a idade é {self.idade}")

@dataclass
class Aluno(Pessoas):
    matricula:str
    curso:str

    def estudando(self):
        print(f"O aluno matriculado em {self.matricula} esta estudando {self.curso}")

@dataclass
class Professor(Pessoas):
    salario: float
    disciplina: str

    def lecionar(self):
        print(f"O professor esta lecionando {self.disciplina}")