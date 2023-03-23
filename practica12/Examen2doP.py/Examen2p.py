import tkinter as tk
from tkinter import messagebox
import random


def imprimir():
    
    nombre = entry_nombre.get()[:2]
    apellidos = entry_apellidos.get()[:2]
    anio_nacimiento = entry_anio_nacimiento.get()[:2]
    anio_actual = entry_anio_actual.get()[:2]
    carrera = entry_carrera.get()[:2]
    numero_aleatorio = str(random.randint(10, 99))

    messagebox.showinfo("Resultados", 
                        f"Nombre: {nombre}\n"
                        f"Apellidos: {apellidos}\n"
                        f"Año de nacimiento : {anio_nacimiento}\n"
                        f"Año actual : {anio_actual}\n"
                        f"Carrera : {carrera}\n"
                        f"Número aleatorio (: {numero_aleatorio}")


ventana = tk.Tk()


label_nombre = tk.Label(ventana, text="Nombre:")
entry_nombre = tk.Entry(ventana)

label_apellidos = tk.Label(ventana, text="Apellidos:")
entry_apellidos = tk.Entry(ventana)

label_anio_nacimiento = tk.Label(ventana, text="Año de nacimiento:")
entry_anio_nacimiento = tk.Entry(ventana)

label_anio_actual = tk.Label(ventana, text="Año actual:")
entry_anio_actual = tk.Entry(ventana)

label_carrera = tk.Label(ventana, text="Carrera:")
entry_carrera = tk.Entry(ventana)

boton_imprimir = tk.Button(ventana, text="Imprimir", command=imprimir)


label_nombre.grid(row=0, column=0)
entry_nombre.grid(row=0, column=1)

label_apellidos.grid(row=1, column=0)
entry_apellidos.grid(row=1, column=1)

label_anio_nacimiento.grid(row=2, column=0)
entry_anio_nacimiento.grid(row=2, column=1)

label_anio_actual.grid(row=3, column=0)
entry_anio_actual.grid(row=3, column=1)

label_carrera.grid(row=4, column=0)
entry_carrera.grid(row=4, column=1)

boton_imprimir.grid(row=5, column=1)


ventana.mainloop()