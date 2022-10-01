from tkinter import *
from PIL import ImageTk, Image
import playsound  # pip install playsound==1.2.2
import time

root = Tk()
root.title("Frames")
img1 = ImageTk.PhotoImage(Image.open("imgs_8/im1.jpg"))
img2 = ImageTk.PhotoImage(Image.open("imgs_8/im2.gif"))


def botao():
    global img1
    root.attributes('-fullscreen', True)
    frame.pack_forget()
    imagem = Label(root, image=img1)
    imagem.grid(row=0, column=0)
    botao_grito = Button(root, text="Fechar",  command=lambda: botao_2(imagem, botao_grito), bd=2, borderwidth=5, bg="#91F125")
    botao_grito.grid(row=1, column=0, sticky=W+E)
    root.mainloop()
    time.sleep(1.5)
    playsound.playsound("imgs_8/musica.mp3")


def botao_2(imagem, botao_grito):
    global img2
    playsound.playsound("imgs_8/musica.mp3")
    imagem.grid_forget()
    imagem= Label(root, image=img2)
    imagem.grid(row=0, column=0)
    botao_grito.grid_forget()
    root.attributes('-fullscreen', False)
    button1 = Button(root, text="Fechar, agora é sério",  command=root.destroy, bd=2, borderwidth=5, bg="#91F125")
    button1.grid(row=1, column=0, sticky=W+E)
    return

frame = LabelFrame(root, text= "Esse é o meu frame...", padx=20, pady=20)
frame.pack(padx=50, pady=50)

l= Label(frame, text="É sério!", fg="red")
b = Button(frame, text="Não aperte esse botão", command=botao)
b.grid(column=0, row=0)
l.grid(column=1, row=1)

root.mainloop()
