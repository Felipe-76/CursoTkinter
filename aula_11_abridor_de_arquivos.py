from tkinter import*
from PIL import ImageTk, Image
from tkinter import filedialog

root=Tk()
root.title("Arquivos")
root.iconbitmap("imgs_7/gallery.ico")


def selecionar_arquivo():
    global imagem
    global my_img
    my_img.pack_forget()
    root.filename = filedialog.askopenfilename(initialdir=r"C:\Users\felip\OneDrive\Área de Trabalho\Programacao\Python\CursoTkinter\imgs_7", title="Selecione o arquivo", filetypes= (("jpeg files", "*.jpeg"), ("all files", "*.*"), ("ico files", "*.ico")))
    imagem = ImageTk.PhotoImage(Image.open(root.filename))
    my_img = Label(root, image=imagem, width=400, height=500)
    my_img.pack()


# Inicializando a imagem vazia para poder realizar o .pack_forget dentro da função possibilitando repetir o processo
my_img = Label()

# Botão para abrir seletor
botao_abrir = Button(root, text="Abrir", command=selecionar_arquivo, bd=3, borderwidth=2, relief=RAISED)
botao_abrir.pack(pady=50, fill=X)

root.mainloop()
