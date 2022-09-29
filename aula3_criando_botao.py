from tkinter import *

root = Tk()


def myClick():
    myLabel = Label(root, text="Apertei o Botão!")
    myLabel.pack()


myButton = Button(root, text="Click Me!", padx=20, pady =40, command = myClick, fg="#ffffff", bg="red")
# padx e pady denotam o tamanho do botão
# fg: foreground color, bg: background color (poderiam ser substituidos pelo nome completo Ex: fg -> foreground)
myButton.pack()


root.mainloop()

"""
Um Erro muito comum: caso fizéssemos assim para definir o comando:

myButton = Button(root, text="Click Me!", padx=20, pady =40, command = myClick())

ao rodar o programa a janela já seria gerada com a funcao do comando executada e 
nao conseguiriamos executar ela de novo clicando no botão.
"""
