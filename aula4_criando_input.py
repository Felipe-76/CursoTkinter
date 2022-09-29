from tkinter import *

root = Tk()

# Janela de entrada de dados
e = Entry(root, width=30, bg="yellow", borderwidth=3)
e.pack()
e.insert(0, "Insira seu nome: ")  # Para deixar um texto inicial dentro da caixa

def myClick():
    myLabel = Label(root, text="Oi " + e.get())  # Aqui foi incluido e.get() que pega dado do campo de entrada
    myLabel.pack()


myButton = Button(root, text="Click Me!", padx=20, pady =40, command = myClick, fg="#ffffff", bg="red")

myButton.pack()


root.mainloop()

"""
Linhas de conteúdo novo: 5-8 e 11
"""
