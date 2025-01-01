from tkinter import*

root = Tk()

root.geometry('500x300')
root.title('Calculadora de IMC')
root.config(bg='lightblue')
#Cor e fonte global
fonte = ('Arial', 14)
letra = 'white'

resultado = Label(root, text='', fg=letra, bg='lightblue', font=fonte)

def calcular_imc(): 
    peso = float(entrada_peso.get())
    altura = float(entrada_altura.get())  / 100
    imc = peso / (altura ** 2)
    resultado.config(text=f'O seu IMC é de: {imc:.2f}')
    resultado.grid(row=3, column=1, pady=15)

label_peso = Label(text='Digite o seu peso.' , fg=letra, bg='lightblue', font=fonte)
label_peso.grid(row=0, column=0, pady=10)

entrada_peso = Entry(root, font=fonte)
entrada_peso.grid(row=0, column=1, pady=10)
print(entrada_peso)

label_altura = Label(text='Digite a sua altura.', fg=letra, bg='lightblue', font=fonte)
label_altura.grid(row=1, column=0, pady=10)

entrada_altura = Entry(root, font=fonte)
entrada_altura.grid(row=1, column=1, pady=10)
print(entrada_altura)

botao = Button(root, text="Calcular IMC", command=calcular_imc, bg='blue', fg=letra, font=fonte)
botao.grid(row=3, column=0, pady=15)

resultado.grid(row=3, column=1, pady=15)

root.mainloop()


