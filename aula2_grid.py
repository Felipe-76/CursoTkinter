from tkinter import *

root = Tk()

# Creating Label Widget
mylabel1 = Label(root, text="Hello World")
mylabel2 = Label(root, text="Meu nome é Felipe Leitão")

# Shoving the label inside the window
mylabel1.grid(row=0, column=0)
mylabel2.grid(row=1, column=1)


root.mainloop()

"""
OBS: Dessa maneira quando expandimos a janela o texto não se ajusta
Entretanto, caso não tenha um dado em uma "celula" ela terá um tamanho
nulo, de forma que se o codigo fosse da seguinte forma:
mylabel1.grid(row=0, column=0)
mylabel2.grid(row=1,column=5)
ficaria da mesma maneira como ficou no código
"""
