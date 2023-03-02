from tkinter import Tk,Frame,Button,messagebox
ventana= Tk()


ventana.title("Practica 12")
ventana.geometry("400x200")
seccion1=Frame(ventana, bg="#F0F8FF")
seccion1.pack(expand=True,fill='both')
def mostrarMensaje():
     messagebox.showinfo("aviso","este mensaje es para avisar algo")("Login")



def agregarBoton():
    botonzul.config(text="+",bg="red",fg="Blue")
    botonNuevo=Button(seccion1,text="Login",bg="000000",fg="blue")
    botonNuevo.pack()

botonzul= Button(seccion1,text="Login",fg="red",command=mostrarMensaje)
botonzul.pack()
    
    



#Mainloop
ventana.mainloop()
