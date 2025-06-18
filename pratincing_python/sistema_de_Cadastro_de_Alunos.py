"""
Wellington Pereira luiz - 26-01-2025 - PT-BR
"""
soma = 0
teste = []
nota_aluno = []
alunos = {'nome':'nome', 'idade':'idade', 'nota':[], 'nota_media':'nota_media', 'situacao':'situacao'}
quantidade = int(input("Deseja add quantos alunos? (Maximo 5!!!)"))

for i in range(quantidade):
    nome_aluno = input(f"\nDigite o nome do {i+1} aluno: ")
    idade_aluno = int(input(f"\nDigite a idade do {i+1} aluno: "))
    for i in range(4):
        nota = int(input(f"\nDigite a nota da {i+1}° materia do {nome_aluno}:"))
        nota_aluno.append(nota)
        soma += nota

    media = soma / 4
    if media >= 7:
        situacao = "Aprovado"
    elif media < 7 and media >= 5:
        situacao = "Recuperacao"
    elif media < 5:
        situacao = "reprovado"
    else:
        print("Nota invalida!")

    alunos = {'nome':nome_aluno, 'idade': idade_aluno, 'nota': nota_aluno, 'nota_media':media, 'situacao': situacao}
    teste.append(alunos)
   


print(teste)






# #IA
# # Definindo o cabeçalho
# print("Wellington Pereira Luiz - 26-01-2025 - PT-BR")

# # Lista para armazenar os dados de todos os alunos
# teste = []

# # Solicita ao usuário o número de alunos a serem cadastrados (máximo 5)
# quantidade = int(input("Deseja adicionar quantos alunos? (Máximo 5!!!): "))

# # Valida a quantidade de alunos
# if quantidade > 5:
#     print("O número máximo de alunos é 5!")
# else:
#     for i in range(quantidade):
#         # Inicializando as variáveis
#         soma = 0
#         nota_aluno = []

#         # Recebendo os dados do aluno
#         nome_aluno = input(f"\nDigite o nome do {i+1}º aluno: ")
#         idade_aluno = int(input(f"\nDigite a idade do {i+1}º aluno: "))

#         # Recebendo as notas do aluno
#         for j in range(4):
#             nota = int(input(f"\nDigite a {j+1}ª nota da matéria do {nome_aluno}: "))
#             nota_aluno.append(nota)
#             soma += nota

#         # Calculando a média
#         media = soma / 4

#         # Determinando a situação do aluno
#         if media >= 7:
#             situacao = "Aprovado"
#         elif media >= 5:
#             situacao = "Recuperação"
#         else:
#             situacao = "Reprovado"

#         # Criando o dicionário do aluno
#         aluno = {
#             'nome': nome_aluno,
#             'idade': idade_aluno,
#             'nota': nota_aluno,
#             'nota_media': media,
#             'situacao': situacao
#         }

#         # Adicionando o aluno na lista de teste
#         teste.append(aluno)

#     # Imprimindo os dados dos alunos cadastrados
#     print("\nDados dos alunos cadastrados:")
#     for aluno in teste:
#         print(f"\nAluno: {aluno['nome']}")
#         print(f"Idade: {aluno['idade']}")
#         print(f"Notas: {aluno['nota']}")
#         print(f"Média: {aluno['nota_media']}")
#         print(f"Situação: {aluno['situacao']}")
