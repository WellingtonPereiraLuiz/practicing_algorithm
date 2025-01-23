from collections import deque

fila = deque()
pilha = []

for contador in range(5):

    valor = int(input(f'Digite o {contador + 1}° valor:'))

    if valor % 2 == 0: 
        fila.append(valor)
    else: 
        pilha.append(valor) 

print("\nElementos da fila:")
while fila:
    valor = fila.popleft()
    print(f'Valor -> {valor}')

print("\nElementos da pilha:")
while pilha:
    valor = pilha.pop()
    print(f'Valor -> {valor}')

    
print("\nEstado final:")
print(f"A sua fila: {list(fila)}") 
print(f"A sua pilha: {pilha}") 