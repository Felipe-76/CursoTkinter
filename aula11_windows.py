from cProfile import label
from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Janela Principal")
root.geometry("400x400")


def abrir():
    global img  # Para a imagem ser reconhecida no tkinter no mainloop ela precisa ser declarada globalmente
    top = Toplevel()  # Usamos TopLevel para outras janelas e nao outras instancias de Tk()
    top.title("2a Janela")
    top.iconbitmap("imgs_6/trophy_cup_512.ico")
    top.geometry("400x600")
    img = ImageTk.PhotoImage(Image.open("imgs_7/im2.jpeg"))
    imagem = Label(top, image=img)
    imagem.grid(row=1, column=0)
    botao = Button(top, text="Fechar 2a janela", command=top.destroy)
    botao.grid(column=0, row=0)

botao = Button(root, text="Abrir outra janela", command=abrir)
botao.pack()

root.mainloop()
