"""
Wellington Pereira Luiz - 23_12_2024
Trabalhando com pilhas e compreendo seus conceitos basicos
"""
"""

#Feito por mim
#Busquei aplicar o conceito de adicionar valores e remover valores de uma pilha e a visualizacao da mesma
pilha = []
pilha.append(4242)
pilha.append(657)
pilha.append(11)
print('----------------------------------------------------')
print(f'--------- {"Seja bem-vindo!".center(36)} -----')
print('----------------------------------------------------')
print('Pilha atual')
for i in range(len(pilha)):
    print(pilha[i])


print('Escolha uma das opções a seguir:')
escolha = int(input(('1 - Adicionar valor na pilha\n2 - Remover valor da pilha\n0 - Sair\n')))

if escolha == 1: 
    add = int(input(('Digite o valor que deseja adicionar:')))
    pilha.append(add)
if escolha == 2: pilha.pop()
"""

#Corrigido pela IA
print('Pilha atual')
for i in range(len(pilha)):
    print(pilha[i])

pilha = []
pilha.append(4242)
pilha.append(657)
pilha.append(11)

print('----------------------------------------------------')
print(f'--------- {"Seja bem-vindo!".center(36)} -----')
print('----------------------------------------------------')

print('Pilha atual:')
for item in pilha:
    print(item)

# Solicitar ao usuário escolher uma opção
print('Escolha uma das opções a seguir:')
try:
    escolha = int(input('1 - Adicionar valor na pilha\n2 - Remover valor da pilha\n0 - Sair\n'))
except ValueError:
    print("Entrada inválida. Por favor, insira um número válido.")
    escolha = -1  # Definir valor inválido para garantir que o código não siga com a execução

if escolha == 1: 
    try:
        add = int(input('Digite o valor que deseja adicionar: '))
        pilha.append(add)
        print(f'{add} foi adicionado à pilha.')
    except ValueError:
        print("Valor inválido. Por favor, insira um número válido.")
elif escolha == 2:
    if pilha:  # Verifica se a pilha não está vazia
        pilha.pop()
        print("Valor removido da pilha.")
    else:
        print("A pilha está vazia. Nenhum valor para remover.")
elif escolha == 0:
    print("Saindo do programa.")
else:
    print("Opção inválida. Tente novamente.")

# Exibir a pilha após a operação
print('Pilha atual:')
for item in pilha:
    print(item)
