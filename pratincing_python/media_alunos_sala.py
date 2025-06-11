#Sistema que calcula media do aluno na sala
#Serao 4 salas, aonde cada sala ira ter uma quantia X de alunos
#Sera feita a media de cada sala e encontrar o melhor aluno de cada sala e mostra na tela
#Apos mostrar o melhor aluno das 4 salas e comparar as notas desses quatro alunos nas materias
#Serao apenas 4 materias, portugues, matematica, fisica, geografia. 
#minino de ponots sera 0, minino para passar sera 6 e maximo de nota sera 10
#Tambem mostre quantos alunos passaram e quandos reprovaram em cada sala

# Pergunta a quantidade de alunos por sala
quantidade_alunos = int(input("Qual é a quantia de alunos por sala? "))

# Exemplo para uma sala (você pode repetir para as outras salas depois)
sala1 = []

for i in range(quantidade_alunos):
    print(f"\nAluno {i+1}:")
    notas = []
    for materia in ["Português", "Matemática", "Física", "Geografia"]:
        nota = float(input(f"Digite a nota de {materia}: "))
        notas.append(nota)
    sala1.append(notas)