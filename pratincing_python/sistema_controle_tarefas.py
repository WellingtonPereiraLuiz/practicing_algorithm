# Crie uma classe chamada ListaDeTarefas
# Essa classe deve:

# Armazenar uma lista de objetos Tarefa

# Ter métodos para:

# Adicionar nova tarefa

# Marcar uma tarefa como concluída

# Listar todas as tarefas

# Listar apenas as tarefas pendentes

# No código principal (fora das classes), simule interações usando:

# Um loop para exibir um menu com opções (adicionar tarefa, listar, etc)

# Estruturas condicionais (if, elif, etc) para decidir o que fazer com base na opção do usuário

# Um laço de repetição para permitir que o usuário execute múltiplas ações até decidir sair


from dataclasses import dataclass

@dataclass
class Tarefa:
    titulo: str
    prioridade: str
    concluida: bool = False

    def marcar_concluida(self):
        self.concluida = True

@dataclass
class ListaDeTarefas:
    tarefas: list[Tarefa] = None

    def __post_init__(self):
        if self.tarefas is None:
            self.tarefas = []

    def adicionar_tarefa(self, titulo: str, prioridade: str):
        nova_tarefa = Tarefa(titulo=titulo, prioridade=prioridade)
        self.tarefas.append(nova_tarefa)

    def marcar_tarefa_concluida(self, titulo: str):
        for tarefa in self.tarefas:
            if tarefa.titulo == titulo:
                tarefa.marcar_concluida()
                return
        print(f"Tarefa '{titulo}' não encontrada.")

    def listar_tarefas(self):
        for tarefa in self.tarefas:
            status = "Concluída" if tarefa.concluida else "Pendente"
            print(f"{tarefa.titulo} - Prioridade: {tarefa.prioridade} - Status: {status}")

    def listar_tarefas_pendentes(self):
        for tarefa in self.tarefas:
            if not tarefa.concluida:
                print(f"{tarefa.titulo} - Prioridade: {tarefa.prioridade}")