from textwrap import fill
from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Image Viewer")
root.iconbitmap("imgs_7/gallery.ico")
pagina = 0


def passar_esquerda():
    global pagina
    pagina -= 1
    colocar_imagem(pagina)


def passar_direita():
    global pagina
    pagina += 1
    colocar_imagem(pagina)


def colocar_imagem(pag):
    global label_contador
    global imagem
    imagem.grid_forget()
    imagem = Label(image = imgs[pag%5], width=400, height=500)
    imagem.grid(column=0, row=0, columnspan=4)
    # Mudar numero da pagina
    label_contador.grid_forget()
    label_contador = Label(text=f"{pag%5+1}")
    label_contador.grid(column=1, row=1)



# Passando as imagens
img_1 = ImageTk.PhotoImage(Image.open("imgs_7/im1.jpeg"))
img_2 = ImageTk.PhotoImage(Image.open("imgs_7/im2.jpeg"))
img_3 = ImageTk.PhotoImage(Image.open("imgs_7/im3.jpeg"))
img_4 = ImageTk.PhotoImage(Image.open("imgs_7/im4.jpeg"))
img_5 = ImageTk.PhotoImage(Image.open("imgs_7/im5.jpeg"))
imgs = [img_1, img_2, img_3, img_4, img_5]
imagem = Label(image = imgs[pagina%5], width=400, height=500)

# Colocando as imagens
imagem.grid(column=0, row=0, columnspan=4)

# Criando os botões e o contador
button_esquerda = Button(text="<", padx=5, pady=5, command=passar_esquerda)
label_contador = Label(text=f"{pagina+1}")
button_fechar = Button(text="Close app", padx=70,pady=5, command=root.destroy)
button_direita = Button(text=">", padx=5, pady=5, command=passar_direita)

# Colocando o Menu
button_esquerda.grid(column=0, row=1)
label_contador.grid(column=1, row=1)
button_fechar.grid(column=2, row=1)
button_direita.grid(column=3, row=1)


root.mainloop()
