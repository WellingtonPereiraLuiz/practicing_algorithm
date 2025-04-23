a = input("Digite a entrada:")
f = ()
c = 0
soma = 0 
for caracatere in a:
    if ord(caracatere) >= 0x4E00 and ord(caracatere) <= 0x9FAF:
        f = caracatere
        for frequencia in a:
            if f(c) == frequencia:
                soma += 1
            c += 1 

print(soma)




# Tua lógica tava querendo fazer isso:

# "Pra cada caractere, verifica se é kanji. Se for, vê quantas vezes ele aparece, soma isso tudo e depois mostra o mais frequente."

# Mas faltou:

# Um dicionário pra registrar quantas vezes cada um apareceu

# Comparação direta (você tentou usar a variável como função)

# Evitar somar tudo num lugar só (soma) e sim por caractere