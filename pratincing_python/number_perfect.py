number = int(input("Digite um numero qualquer."))
soma = 0
for i in range(1, number):
    if number % (i) == 0 :
       soma += i


if soma == number:
    print(f"O numero {number} é perfeito. Pois a soma dos seus divisores é {soma}") 
else:
    print(f"O numero {number} não é perfeito. Pois a soma dos seus divisores é {soma}") 
    