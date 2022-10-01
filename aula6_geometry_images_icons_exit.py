from cProfile import label
from tkinter import *
from PIL import ImageTk, Image  # pip install Pillow

root = Tk()
root.title("Aula 6")

# Adquirir tamanho da tela
screen_width = root.winfo_screenwidth()
# print(f"{screen_width}")
screen_height = root.winfo_screenheight()
root.geometry(f"{screen_width}x{screen_height}")

# Ícone do programa (.ico (16x16), (32x32), (64x64))
endereco = ("imgs_6/trophy_cup_512.ico")
root.iconbitmap(endereco)

# Botao de quit
botao = Button(root, text="Fechar programa", command=root.destroy, bg="red", pady=20, padx=30)
# root.exit também é uma opção, porém tem algumas ressalvas.
botao.pack()

# Imagens (Tkinter suporta nativamente .gif e outro formato obsoleto)
# Para usar as imagens mais utilizadas (.png e .jpeg) é preciso importar a Pillow (PIL melhorada), mas continua sendo PIL
# Ver linha 2

my_img =  ImageTk.PhotoImage(Image.open("imgs_6/img_1.png"))
my_label = Label(image=my_img)
my_label.pack()  # Caso a geometria não tivesse sido definida na linha 12 a janela teria o tamanho da foto

root.mainloop()
