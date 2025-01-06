from tkinter import *

# Configuração principal da janela
root = Tk()
root.geometry('500x300')
root.title('Calculadora de IMC')
root.config(bg='lightblue')

# Configurações globais
fonte = ('Arial', 14)
letra = 'white'

# Funções auxiliares
def calcular_imc():
    try:
        peso = float(entrada_peso.get())
        altura = float(entrada_altura.get()) / 100
        imc = peso / (altura ** 2)

        # Determinar a cor com base no IMC
        if imc < 18.5:
            cor = 'yellow'
        elif 18.5 <= imc < 24.9:
            cor = 'green'
        elif 25 <= imc < 29.9:
            cor = 'orange'
        else:
            cor = 'red'

        resultado.config(text=f'O seu IMC é de: {imc:.2f}', fg=cor)
    except ValueError:
        resultado.config(text='Por favor, insira valores válidos.', fg='red')

def on_enter(e):
    botao['bg'] = 'darkblue'

def on_leave(e):
    botao['bg'] = 'blue'

def clear_placeholder(event, entry):
    if entry.get() in ('Digite o peso em kg', 'Digite a altura em cm'):
        entry.delete(0, 'end')

# Estrutura de layout
frame = Frame(root, bg='lightblue')
frame.pack(pady=20, padx=20)

# Widgets
label_peso = Label(frame, text='Digite o seu peso:', fg=letra, bg='lightblue', font=fonte)
label_peso.grid(row=0, column=0, pady=10, padx=20)

entrada_peso = Entry(frame, font=fonte)
entrada_peso.grid(row=0, column=1, pady=10, padx=20)
entrada_peso.insert(0, 'Digite o peso em kg')
entrada_peso.bind('<FocusIn>', lambda event: clear_placeholder(event, entrada_peso))

label_altura = Label(frame, text='Digite a sua altura:', fg=letra, bg='lightblue', font=fonte)
label_altura.grid(row=1, column=0, pady=10, padx=20)

entrada_altura = Entry(frame, font=fonte)
entrada_altura.grid(row=1, column=1, pady=10, padx=20)
entrada_altura.insert(0, 'Digite a altura em cm')
entrada_altura.bind('<FocusIn>', lambda event: clear_placeholder(event, entrada_altura))

botao = Button(frame, text="Calcular IMC", command=calcular_imc, bg='blue', fg=letra, font=fonte)
botao.grid(row=2, column=0, columnspan=2, pady=20)
botao.bind("<Enter>", on_enter)
botao.bind("<Leave>", on_leave)

resultado = Label(frame, text='', fg=letra, bg='lightblue', font=fonte)
resultado.grid(row=3, column=0, columnspan=2, pady=10)

# Iniciar o loop principal
root.mainloop()


# faca com que o campo de altura e peso desapareca e apareca a mensagem assim que o mouse passar por cima.
#Coloque algumas imagens e trabalhe com elas
# Implemente a questao da altura e nome, aramazene isso e de a opcao para visualizar o historico de calculos
#Coloque uma mensagem personalizada para cada nivel de imc, como tais: magro, obeso, morbido e etc...
