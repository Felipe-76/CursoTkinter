from tkinter import *

root = Tk()
root.title("Oi Mundo")

# Creating Label Widget
mylabel = Label(root, text="Hello World")

# Shoving the label inside the window
mylabel.pack()

root.mainloop()

"""
Em Tkinter tudo é feito em duas etapas, primeiro se cria o widget e
em seguida ele é inserido na interface gráfica.

Como python é orientado a objetos o seguinte teria igual efeito:
mylabel = Label(root, text="Hello World").pack()
"""
