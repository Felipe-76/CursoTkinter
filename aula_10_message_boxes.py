from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Message box")


# Diferentes caixas de mensagem: showinfo, showwarning, showerror, askquestion, askokcancel, askyesno
def popup():
    resposta = messagebox.askyesno("Título", "Mensagem")
    if resposta == 1:
        Label(root, text="Você apertou no sim").pack()
    else:
        Label(root, text="Você apertou no não").pack()


Button(root, text="Mostrar", command=popup).pack()

root.mainloop()
