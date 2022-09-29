from tkinter import *

root = Tk()
root.title("Calculadora")

# Janela de entrada de dados
e = Entry(root, width=35, borderwidth=5, )
e.grid(row=0, column=0, columnspan=3, padx=10, pady=5)  # Columnspan é para determinar a quantidade de celulas ocupadas embaixo

estado = None

def button_click(num):
    #e.delete(0, END)
    atual = e.get()
    e.delete(0, END)
    e.insert(0, str(atual) + str(num))


def button_limpar():
    global estado
    estado = "CE"
    e.delete(0, END)


def button_somar():
    if(e.get() == ""):
        e.insert(0, "Número 1 não inserido, clique em clear")
    else:
        global estado
        estado = "soma"
        primeiro_numero = e.get()
        global num_1
        num_1 = int(primeiro_numero)
        e.delete(0, END)

    
def button_igual():
    if(e.get() == ""):
        e.insert(0, "Número 1 não inserido, clique em clear")
    else:
        num_2 = int(e.get())
        global num_1
        e.delete(0, END)
        if(estado == "soma"):
            resultado = num_1 + num_2
            e.insert(0, resultado)
        elif(estado == "subtracao"):
            resultado = num_1 - num_2
            e.insert(0, resultado)
        elif(estado == "multiplicacao"):
            resultado = num_1 * num_2
            e.insert(0, resultado)
        elif(estado == "divisao"):
            if(num_1 == 0 and num_2 == 0):
                e.insert(0, "Erro, divisao por zero, clique em Clear")
                resultado = None
            else:
                resultado = int(num_1 / num_2)
                e.insert(0, resultado)


def button_subtract():
    if(e.get() == ""):
        e.insert(0, "Número 1 não inserido, clique em clear")
    else:   
        primeiro_numero = e.get()
        global num_1
        num_1 = int(primeiro_numero)
        e.delete(0, END)    
        global estado
        estado = "subtracao"


def button_multiply():
    if(e.get() == ""):
        e.insert(0, "Número 1 não inserido, clique em clear")
    else:
        primeiro_numero = e.get()
        global num_1
        num_1 = int(primeiro_numero)
        e.delete(0, END)
        global estado
        estado = "multiplicacao"


def button_divide():
    if(e.get() == ""):
        e.insert(0, "Número 1 não inserido, clique em clear")
    else:
        primeiro_numero = e.get()
        global num_1
        num_1 = int(primeiro_numero)
        e.delete(0, END)
        global estado
        estado = "divisao"


# Criando os botões
botao1= Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1), borderwidth=3)
botao2= Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2), borderwidth=3)
botao3= Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3), borderwidth=3)
botao4= Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4), borderwidth=3)
botao5= Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5), borderwidth=3)
botao6= Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6), borderwidth=3)
botao7= Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7), borderwidth=3)
botao8= Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8), borderwidth=3)
botao9= Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9), borderwidth=3)
botao0= Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0), borderwidth=3)
botao_soma = Button(root, text="+", padx=39, pady=20, command=button_somar, borderwidth=3)
botao_subtrair = Button(root, text= "-", padx = 40, pady=20, command=button_subtract, borderwidth=3)
botao_igual = Button(root, text="=", padx=39, pady=20, command=button_igual, borderwidth=3)
botao_multiplicar = Button(root, text= "*", padx = 40, pady=20, command=button_multiply, borderwidth=3)
botao_dividir = Button(root, text= "/", padx = 40, pady=20, command=button_divide, borderwidth=3)
botao_limpar = Button(root, text="Clear (C)", width=27,  padx=39, pady=5, command=button_limpar, borderwidth=3)



# Posicionando os botões
botao9.grid(column=2, row=1)
botao8.grid(column=1, row=1)
botao7.grid(column=0, row=1)

botao6.grid(column=2, row=2)
botao5.grid(column=1, row=2)
botao4.grid(column=0, row=2)

botao3.grid(column=2, row=3)
botao2.grid(column=1, row=3)
botao1.grid(column=0, row=3)

botao0.grid(column=1, row=4)
botao_soma.grid(column=0, row=4)
botao_subtrair.grid(column=2, row=4)

botao_multiplicar.grid(column=0, row=5, pady=3)
botao_dividir.grid(column=1, row=5, pady=3)
botao_igual.grid(column=2, row=5, pady=3)

botao_limpar.grid(column=0, row=6, pady=3, columnspan=3)


root.mainloop()


"""
Calculadora de inteiros, foi necessário restringir para inteiros para não tratar o erro no caso
de continuar a escrever um número depois de aparecer um resultado float no visor.
"""
