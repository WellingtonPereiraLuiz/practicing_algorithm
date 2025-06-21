import hashlib

class Usuario:
    def __init__(self, nome_usuario, idade_usuario):
        self.nome_usuario = nome_usuario
        self.idade_usuario = idade_usuario
        self._senha_hash = None

    @property
    def nome_usuario(self):
        return self._nome_usuario 

    @nome_usuario.setter 
    def nome_usuario(self, valor):
        if valor: 
            self._nome_usuario = valor
        else:
            print("Erro: O nome de usuário não pode ser vazio!")

    @property
    def idade_usuario(self):
        return self._idade_usuario

    @idade_usuario.setter 
    def idade_usuario(self, valor):
        if valor > 0 and valor <= 120:
            self._idade_usuario = valor
        else:
            print("Erro: A idade do usuário não pode ser menor ou maior que 120 anos!")
    
    def cadastrar_senha(self, senha_texto):
        self._senha_hash = hashlib.sha256(senha_texto.encode('utf-8')).hexdigest()

    def verificar_senha(self, senha_texto):
        senha_hash_verificar = hashlib.sha256(senha_texto.encode('utf-8')).hexdigest()

        if senha_hash_verificar == self._senha_hash:
            print("Senha correta!")
        else:
            print("Senha incorreta!")





class Administrador(Usuario):
    def __init__(self, nome_usuario, nivel_acesso, idade_usuario):
        super().__init__(nome_usuario, idade_usuario)
        self.nivel_acesso = nivel_acesso

    def cadastrar_senha(self, senha_texto):
        super().cadastrar_senha(senha_texto)
        print(f"Senha própria cadastrada pelo administrador {self.nome_usuario} (Nível: {self.nivel_acesso}).")

    def redefinir_senha_usuario(self, usuario_alvo, nova_senha):
        if self.nivel_acesso >= 10:
            usuario_alvo.cadastrar_senha(nova_senha)
            print(f"Administrador {self.nome_usuario} redefiniu a senha do usuário '{usuario_alvo.nome_usuario}'.")
        else:
            print(f"Administrador {self.nome_usuario} não tem permissão para redefinir senhas de outros usuários.")




         
print("--- Testando Classe Usuario ---")
usuario_comum = Usuario("mariazinha", 25)
usuario_comum.cadastrar_senha("senha123")
usuario_comum.verificar_senha("senha123") 
usuario_comum.verificar_senha("senhaerrada") 

print(f"Nome de usuário antes da mudança: {usuario_comum.nome_usuario}")
usuario_comum.nome_usuario = "MariaSilva" 
print(f"Nome de usuário depois da mudança: {usuario_comum.nome_usuario}")
usuario_comum.nome_usuario = "" 
print(f"Nome de usuário após tentar vazio: {usuario_comum.nome_usuario}") 


print(f"Idade do usuário antes da mudança: {usuario_comum.idade_usuario}")
usuario_comum.idade_usuario = 30
print(f"Idade do usuário depois da mudança: {usuario_comum.idade_usuario}")
usuario_comum.nome_usuario = "" 
print(f"Idade do usuário após tentar vazio: {usuario_comum.idade_usuario}") 


print("\n--- Testando Classe Administrador ---")
admin_master = Administrador("superadmin", 10, 40)
admin_master.cadastrar_senha("admin@123") 


usuario_para_reset = Usuario("jose_silva", 50)
usuario_para_reset.cadastrar_senha("senha_antiga")
print(f"Senha de {usuario_para_reset.nome_usuario} antes do reset:")
usuario_para_reset.verificar_senha("senha_antiga")

admin_master.redefinir_senha_usuario(usuario_para_reset, "nova_senha_forte")
print(f"Senha de {usuario_para_reset.nome_usuario} depois do reset:")
usuario_para_reset.verificar_senha("nova_senha_forte") 
usuario_para_reset.verificar_senha("senha_antiga") 


admin_junior = Administrador("joao_ajudante", 5, 30)
admin_junior.redefinir_senha_usuario(usuario_comum, "alguma_senha") 