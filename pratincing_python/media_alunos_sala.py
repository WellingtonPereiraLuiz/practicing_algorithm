#Sistema que calcula media do aluno na sala
#Serao 4 salas, aonde cada sala ira ter uma quantia X de alunos
#Sera feita a media de cada sala e encontrar o melhor aluno de cada sala e mostra na tela
#Apos mostrar o melhor aluno das 4 salas e comparar as notas desses quatro alunos nas materias
#Serao apenas 4 materias, portugues, matematica, fisica, geografia. 
#minino de ponots sera 0, minino para passar sera 6 e maximo de nota sera 10
#Tambem mostre quantos alunos passaram e quandos reprovaram em cada sala


sala = []
salas = []
print("Bem vindo ao sistema de media dos alunos")
alunos_por_sala = {'nome': '', 'nota1': 0, 'nota2': 0, 'nota3': 0, 'nota4': 0, 'media': 0, 'situacao': ''}

for i in range(2):
    Quantidade_alunos = int(input(f"Qual e a quantia de alunos na sala{i + 1}?"))
    for t in range(Quantidade_alunos):
        aluno = alunos_por_sala.copy()
        aluno["nome"] = input(f'Digite o nome do aluno:')
        aluno["nota1"] = float(input(f'Digite a nota de matematica:'))
        aluno["nota2"] = float(input(f'Digite a nota de ingles:'))
        aluno["nota3"] = float(input(f'Digite a nota de portugues:'))
        aluno["nota4"] = float(input(f'Digite a nota de geografia:'))

        aluno["media"] = (aluno["nota1"] + aluno["nota2"] + aluno["nota3"] + aluno["nota4"]) / 4
        
        if aluno['media'] >= 6:
            aluno['situacao'] = 'aprovado'
        else:
            aluno['situacao'] = 'reprovado'

        
    salas.append(sala)


print(alunos_por_sala)
print(salas)

