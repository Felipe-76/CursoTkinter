from tkinter import *

root = Tk()
root.title("radio")

def clicked(value):
    global mylabel
    mylabel.pack_forget()
    mylabel = Label(root, text=value)
    mylabel.pack()


r = IntVar()
# Tkinter variables are quite different than Python standard variables
# This way we can use r.set() and r.get()
r.set(2)

# # Esses botões compartilham a variável r, cada um com um valor diferente para a mesma.
# Radiobutton(root, text="Option 1", variable=r, value=1, command=lambda: clicked(r.get())).pack()
# Radiobutton(root, text="Option 2", variable=r, value=2, command=lambda: clicked(r.get())).pack()

# Definindo os botões com um loop for:
lista = [
    ("one", 1),
    ("two", 2),
    ("three", 3),
    ("four", 4),
]

for texto, num in lista:
    Radiobutton(root, text=texto, variable=r, value=num).pack(anchor=W)

# Botão para mostrar o valor
mybutton = Button(text= "Me aperta!", command=lambda: clicked(r.get()))
mybutton.pack()

# Valor inicial
mylabel = Label(root, text=r.get())
mylabel.pack()

root.mainloop()
