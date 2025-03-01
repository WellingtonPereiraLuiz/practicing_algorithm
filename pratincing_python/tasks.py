"""
Wellington Pereira Luiz - PT-BR - 17-02
"""

import os

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

tarefas = [
    {"tarefa": "Estudar Python", "concluida": False},
    {"tarefa": "Fazer compras", "concluida": True},
    {"tarefa": "Treinar Muay Thai", "concluida": False},
    {"tarefa": "Revisar código", "concluida": False},
    {"tarefa": "Ler um livro", "concluida": True}
]

while True:
    
    print("Menu de Tarefas.")
    print("1 - Adicionar Tarefa.")
    print("2 - Ver Tarefas.")
    print("3 - Editar Tarefa.")
    print("4 - Concluir Tarefa.")
    print("5 - Excluir Tarefa.")
    print("6 - Sair.")

    escolha = input("Escolha uma das opções:")

    if escolha == "1":
        limpar_tela()
        tarefa = input("Digite a nova tarefa:")
        tarefas.append({'tarefa':tarefa, 'concluida':False})
        input("Clique na tela para voltar ao menu inicial.")
        limpar_tela()

    elif escolha == "2":
        limpar_tela()
        if not tarefas:
            print("Voce nao tem tarefas, adicione algumas para comecar")
            input("Clique na tela para voltar ao menu inicial.")
            limpar_tela()
        else:
           
            for i,t in enumerate(tarefas):
                concluido = "Concluido" if t["concluida"] else "Em andamento"
                print(f"{i+1}. {t["tarefa"]} [{concluido}]")
            input("Clique na tela para voltar ao menu inicial.")
            limpar_tela()
    elif escolha == "3":
        limpar_tela()
        if not tarefas:
            print("Voce nao tem tarefas, adicione algumas para comecar")
            input("Clique na tela para voltar ao menu inicial.")
            limpar_tela()
        else:
            for i,t in enumerate(tarefas):
                
                print(f"{i+1}. {t["tarefa"]} ")

            indice = int(input("Escolha qual tarefa deseja editar.")) - 1
            #mudar o estado da tarefa para "Em andamento" quando editar uma determinada tarefa
            if 0 <= indice < len(tarefas):
                nova_tarefa = input("Escreva a nova descricao da tarefa:")
                tarefas[indice]["tarefa"] = nova_tarefa
                print("Tarefa editada com sucesso paezao!")
                input("Clique na tela para voltar ao menu inicial.")
                limpar_tela()
            else:
                print("Valor invalido")
                input("Clique na tela para voltar ao menu inicial.")
                limpar_tela()
    elif escolha == "4":
        limpar_tela()
        if not tarefas:
            print("Voce nao tem tarefas, adicione algumas para comecar")
            input("Clique na tela para voltar ao menu inicial.")
            limpar_tela()
        else:
            for i,t in enumerate(tarefas):
                print(f"{i+1}. {t["tarefa"]} {t["concluida"]}")

            indice = int(input("Escolha qual tarefa deseja marcar como concluida.")) - 1
            
            if 0 <= indice < len(tarefas):
                 tarefas[indice]["concluida"] = True
                 print("Tarefa marcada como concluida!")
                 input("Clique na tela para voltar ao menu inicial.")
                 limpar_tela()
            else:
                print("Valor invalido")
                input("Clique na tela para voltar ao menu inicial.")
                limpar_tela()
    elif escolha == "5":
        limpar_tela()
        tarefas = [t for t in tarefas if not t["concluida"]]
        print("Tarefas concluídas removidas!")
        input("Clique na tela para voltar ao menu inicial.")
        limpar_tela()
    elif escolha == "6":
        limpar_tela()
        print("Saindo do programa")
        break
    else:
        print("Opção invalida.")
        input("Clique na tela para voltar ao menu inicial.")
        limpar_tela()
    
