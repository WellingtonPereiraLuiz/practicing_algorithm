from cadastrar_usuario import Aluno
from cadastrar_usuario import Professor

aluno1 = Aluno(nome="Joao", idade=12, matricula= "Primeira", curso="ingles" )
professor1 = Professor(nome="Eduardo", idade= 43, salario= 2000, disciplina= "Portugues")

aluno1.apresentar()
professor1.apresentar()
aluno1.estudando()
professor1.lecionar()