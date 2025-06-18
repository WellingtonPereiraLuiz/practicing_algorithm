#Sistema que calcula media do aluno na sala
#Serao 4 salas, aonde cada sala ira ter uma quantia X de alunos
#Sera feita a media de cada sala e encontrar o melhor aluno de cada sala e mostra na tela
#Apos mostrar o melhor aluno das 4 salas e comparar as notas desses quatro alunos nas materias
#Serao apenas 4 materias, portugues, matematica, fisica, geografia. 
#minino de ponots sera 0, minino para passar sera 6 e maximo de nota sera 10
#Tambem mostre quantos alunos passaram e quandos reprovaram em cada sala



sala1 = []
sala2 = []
sala3 = []
sala4 = []

aluno = []

Quantidade_alunos = input(int("Qual e a quantia de alunos por sala?"))

for i in Quantidade_alunos:
    for c in 4:
        aluno = input(int("Digite a nota do "))