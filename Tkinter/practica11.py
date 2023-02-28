
from tkinter import Tk,Frame,Button

#1.Creacion de ventana objeto
ventana= Tk()
ventana.title("Practica 11: #frames")
ventana.geometry("600x400")

#Definimos las secciones de la ventana
seccion1=Frame(ventana, bg="#ffff00")
seccion1.pack(expand=True,fill='both')

seccion2=Frame(ventana, bg="#0066ff")
seccion2.pack(expand=True,fill='both')

seccion3=Frame(ventana, bg="#ffff00")
seccion3.pack(expand=True,fill='both')

seccion4=Frame(ventana, bg="#0066ff")
seccion4.pack(expand=True,fill='both')

#botones
botonzul= Button(seccion1,text="boton azul",fg="blue")
botonzul.place(x=60, y=60)

BotonNegro= Button(seccion2,text="boton negro",fg="#ff6699")
BotonNegro.grid(row=0, column=1)

BotonNegro= Button(seccion2,text="boton verde",fg="green")
BotonNegro.grid(row=0, column=2)

BotonNegro= Button(seccion3,text="boton verde",fg="green",bg="#ff6699")
BotonNegro.grid(row=1, column=1)




#Mainloop
ventana.mainloop()
