nome = input("Digite o nome do aluno: ")
soma = 0
for i in range(4):
    nota = int(input(f"\nDigite a nota da {i+1}° materia do {nome}:"))
    soma += nota

media = soma / 4
if media >= 7:
    print("Aprovado")
elif media < 7 and media >= 5:
    print("Recuperacao")
elif media < 5:
    print("reprovado")
else:
    print("Nota invalida!")