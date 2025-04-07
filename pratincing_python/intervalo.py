valor = float(input("Digite um valor aleatorio: "))

if valor > 0 and valor <= 25.00:
    print("Intervalor 0,25")
elif valor > 25.00 and valor <= 50.00:
    print("Intervalo 25,50")
elif valor > 50.00 and valor <= 100.00:
    print("Intervalo 50,100")
else:
    print("Fora do intervalo")
