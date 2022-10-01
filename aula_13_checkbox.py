from tkinter import *

root = Tk()
root.title("checkboxes")
root.geometry("300x50")


def selecionar():
    global mylabel
    mylabel.pack_forget()
    mylabel = Label(root, text=var.get())
    mylabel.pack()


var = StringVar()
caixa = Checkbutton(root, text="Caixa de seleção", variable=var, command=selecionar, onvalue="on", offvalue="off")  # por padrao seria on = 1 e off = 0
caixa.deselect()  # Quando colocamos strings na caixa de seleção há um pequeno glitch que ela já vem selecionada, por isso essa linha.
caixa.pack()

mylabel = Label(root, text=var.get())
mylabel.pack()

root.mainloop()