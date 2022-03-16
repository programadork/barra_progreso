
from tkinter import *

from tkinter.ttk import Progressbar

import time

def inicio():
    contador = 100
    progreso = 0
    velocidad = 1
    while(progreso<contador):
        time.sleep(0.05)
        barra['value']+=(velocidad/contador)*100
        progreso+=velocidad
        porcentaje.set(str(int((progreso/contador)*100))+"%")
        texto.set(str(progreso)+"/"+str(contador)+" Progreso terminado")
        root.update_idletasks()

root = Tk()
root.title("Barra de progreso")
root.geometry("400x280")
root.config(bg="#109DFA")

porcentaje = StringVar()

texto = StringVar()

barra = Progressbar(root, orient=HORIZONTAL, length=400)
barra.pack(pady=80)

porcentaje_label = Label(root, textvariable=porcentaje).pack()

texto_label = Label(root, textvariable=texto).pack()

boton = Button(root, text="Progreso", width=20,pady=10,command=inicio).pack()


root.mainloop()