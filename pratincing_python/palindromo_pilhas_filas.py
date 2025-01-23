from collections import deque

def eh_palindromo(texto):
   
    texto = ''.join(char.lower() for char in texto if char.isalnum())
  
    fila = deque()
    pilha = []
    

    for char in texto:
        fila.append(char)
        pilha.append(char)
    
 
    while fila:
        if fila.popleft() != pilha.pop():
            return False 
    
    return True  


string = input("Digite uma palavra ou frase: ")

if eh_palindromo(string):
    print(f'"{string}" é um palíndromo!')
else:
    print(f'"{string}" não é um palíndromo.')
