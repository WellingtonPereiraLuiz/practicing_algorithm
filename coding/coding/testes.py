number = int(input("Digite um número inteiro positivo:"))
fatorial = 1
for l in range(1, number + 1):
    fatorial *= l

print(f"O fatorial de {number} é: {fatorial}")

