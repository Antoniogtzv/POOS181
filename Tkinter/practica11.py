
from tkinter import Tk,Frame,Button,messagebox

def mostrarMensaje():
    messagebox.showinfo("aviso","este mensaje es para avisar algo")
    messagebox.showerror("Todo Fallo con exito")
    print(messagebox.askokcancel("pregunta","el o ella jugo con tu corazon"))
    messagebox.askokcancel("ella jugo con tu corazon")

#agregar botones
def agregarBoton():
    botonzul.config(text="+",bg="green",fg="white")
    botonNuevo=Button(seccion3,text="Boton nuevo")
    botonNuevo.pack()


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
botonzul= Button(seccion1,text="boton azul",fg="blue",command=mostrarMensaje)
botonzul.place(x=60, y=60)

BotonNegro= Button(seccion2,text="boton negro",fg="#000000",command=agregarBoton)
BotonNegro.grid(row=0, column=1)

BotonVerde= Button(seccion2,text="boton verde",fg="green")
BotonVerde.grid(row=0, column=2)

BotonRojo= Button(seccion3,text="boton rojo",fg="red",bg="#A52A2A")
BotonRojo.grid(row=1, column=1)




#Mainloop
ventana.mainloop()
