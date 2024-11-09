peso = float(input('Digite o seu peso (em  Kg): '))
altura = float(input('Digite a sua altura (em metros): '))
imc = peso / (altura ** 2)

print(f"Seu IMC é: {imc:.1f}")


if imc < 18.5:
    print("Abaixo do peso")
elif imc >= 18.5 and imc <= 24.9:
    print("Peso normal")
elif imc >= 25 and imc <= 29.9:
    print("Sobrepeso")
elif imc >= 30:
    print("Obesidade")