from tkinter import *
from tkinter import ttk


#Es la ríaz
root = Tk()

#Algunas propiedades
root.title("BANXICO") # Título de la ventana
root.resizable(0,0) #Poder cambiar el tamaño
root.geometry('300x300') #Medida de la ventana

#Frame
frame = Frame(root, width=200, height=200) #Creando el marco
frame.pack(side="top", anchor="w") #Empaqueta el elemento en la raíz si no, no se puede mostrar, paramestros para posición
# frame.pack(fill='x' o 'y' o 'both', expand=1 o 0) rellenar y expandir (se usan con fill=y 0 both) a las dimenciones del padre





root.mainloop() 