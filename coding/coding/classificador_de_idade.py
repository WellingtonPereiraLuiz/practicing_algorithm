while True:
    idade = int(input("Digite a sua idade: "))
    ingresso = 50
    if idade <= 12:
        desconto = (50 / 100) * ingresso 
        print(f"Criança com desconto de 50%. Valor do ingresso: R${desconto}.")
    elif 12 < idade <= 18:
        carteira = input("Possui carteirinha de estudante? (S/N)").upper()
        if carteira == "S":
            desconto = (45 / 100) * ingresso 
            print(f"Jovem com desconto de 45%. Valor do ingresso: R${desconto}.")
        else:
            print(f"Jovem so possui desconto com carteirinha de estudante. Valor do ingresso: R${ingresso} ")
    elif idade > 18:
        print(f"Adulto não possui desconto. Valor do ingresso: R${ingresso}.")
    elif idade > 60:
        desconto = (20 / 100) * ingresso 
        print(f"Adulto com desconto de 20%. Valor do ingresso: R${desconto}")
    else:
        print("Digite uma idade Valida!")
    
    encerrar = (input("Deseja Encerrar? (S/N)")).upper()
    if (encerrar) == "S":
        break
    