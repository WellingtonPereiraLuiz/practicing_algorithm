senha = input("Digite a sua senha: ")

if len(senha) < 8:
    print("Senha inválida! Verifique os critérios:")
    print("- Deve ter pelo menos 8 caracteres.")
elif not any(char.isupper() for char in senha):
    print("Senha inválida! Verifique os critérios:")
    print("- Deve conter pelo menos uma letra maiúscula.")
elif not any(char.islower() for char in senha):
    print("Senha inválida! Verifique os critérios:")
    print("- Deve conter pelo menos uma letra minúscula.")
elif not any(char.isdigit() for char in senha):
    print("Senha inválida! Verifique os critérios:")
    print("- Deve conter pelo menos um número.")
elif not any(char in "!@#$%^&*()-_=+[]{}|;:'\",.<>?/" for char in senha):
    print("Senha inválida! Verifique os critérios:")
    print("- Deve conter pelo menos um caractere especial.")
elif " " in senha:
    print("Senha inválida! Verifique os critérios:")
    print("- Não deve conter espaços.")
else:
    print("Senha válida!")
