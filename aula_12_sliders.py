from tkinter import *


root = Tk()
root.title("Sliders")
root.geometry("300x200")


def slide():
    global my_label
    my_label.pack_forget()
    my_label = Label(root, text=f"{horizontal.get()}x{vertical.get()} = "f"{horizontal.get()* vertical.get()}")
    my_label.pack(side=TOP)
    if (vertical.get()> 50):
        root.geometry(str(horizontal.get()) + "x" + str(vertical.get()))


my_label= Label(text= "Coloque um y maior que 50 e aperte o botão")
my_label.pack(side=BOTTOM)
my_button = Button(root, text="Me aperta", command=slide).pack(side=TOP)

# Slider widget is "Scale"
vertical = Scale(root, from_=0, to=1600)
vertical.pack(side= TOP)  # Scales precisam fazer .pack() separado, nao na mesma linha.

horizontal = Scale(root, from_=0, to=1600, orient=HORIZONTAL)
horizontal.pack(side= TOP)

root.mainloop()
