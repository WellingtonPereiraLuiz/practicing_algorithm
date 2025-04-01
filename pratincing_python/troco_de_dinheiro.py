# Leia um valor inteiro. A seguir, calcule o menor número de notas possíveis (cédulas) no qual o valor pode ser decomposto. 
# As notas consideradas são de 100, 50, 20, 10, 5, 2 e 1. A seguir mostre o valor lido e a relação de notas necessárias.
# Entrada

# O arquivo de entrada contém um valor inteiro N (0 < N < 1000000).
# Saída

# Imprima o valor lido e, em seguida, a quantidade mínima de notas de cada tipo necessárias, conforme o exemplo fornecido.
# Exemplo de Entrada 	

# 576
# Exemplo de Saída

# 576
# 5 nota(s) de R$ 100,00
# 1 nota(s) de R$ 50,00
# 1 nota(s) de R$ 20,00
# 0 nota(s) de R$ 10,00
# 1 nota(s) de R$ 5,00
# 0 nota(s) de R$ 2,00
# 1 nota(s) de R$ 1,00

valor_01 = int(input("Digite um valor qualquer: "))

cedulas = [100, 50, 20 , 10, 5, 2, 1]

for i in cedulas:
    nota =   valor_01 // i
    valor_01 %= i
    print(f"Teste stst {nota}")

