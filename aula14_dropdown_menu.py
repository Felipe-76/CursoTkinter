from tkinter import *


root = Tk()
root.title("Dropdown menu")
root.geometry("400x100")


def show():
    global mylabel
    mylabel.pack_forget()
    mylabel = Label(root, text=var.get())
    mylabel.pack()


dias = ["Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday"
]

var = StringVar()
var.set(dias[0])  # Para definir um valor inicial para a caixa

# Caixa de Seleção
drop = OptionMenu(root, var, *dias)
drop.pack()

botao = Button(root, text="Clique aqui!", command=show)
botao.pack()
mylabel = Label()

root.mainloop()
