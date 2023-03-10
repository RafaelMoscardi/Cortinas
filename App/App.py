from logging import root
from tkinter import *
from typing import final

# -------------------------------------------------------------------------------------------------------
# funções
# C = Altura / Largura
def calcular():
    A = float(textbox1.get())
    L = float(textbox2.get())
    T = L * 6
    VT = T *15
    VL = 55 * L
    VF = A * 22 * T
    C = VF + VT + VL
    final.set(str(f"R$ {C:.2f}"))

# -------------------------------------------------------------------------------------------------------
# GUI
root = Tk()
root.title("CORTINA GALO")

final = StringVar()

# -------------------------------------------------------------------------------------------------------
# widgets
label1=Label(root,text="Altura:",
                font= "Algerian 9",
                fg= "white",
                bg= "purple",
                relief= "solid")
textbox1=Entry(root)
label2=Label(root,text="Largura:",
                font= "Algerian 9",
                fg= "white",
                bg= "purple",
                relief= "solid")
textbox2=Entry(root,
                bg= "white")
button1=Button(root,text="Calcular",
                font= "Algerian 9",
                fg= "white",
                bg= "purple",
                relief= "solid",
                width=17,
                height=2,
                command=calcular)
label_resultado=Label(root,textvariable=final)

# -------------------------------------------------------------------------------------------------------
# layout
label1.grid(row=0, sticky=W)
label2.grid(row=1, sticky=W)
textbox1.grid(row=0, column=1)
textbox2.grid(row=1, column=1)
button1.grid(row=2, column=1)
label_resultado.grid(row=3, column=1)

root.mainloop()