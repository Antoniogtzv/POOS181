import tkinter as tk

# Creamos la ventana principal
ventana = tk.Tk()

# Configuramos el título de la ventana
ventana.title("Mi Ventana")

# Configuramos las dimensiones de la ventana
ventana.geometry("300x200")

# Creamos una etiqueta para mostrar un mensaje
etiqueta = tk.Label(ventana, text="¡Hola, mundo!")
etiqueta.pack()

# Creamos un botón para cerrar la ventana
boton_cerrar = tk.Button(ventana, text="Cerrar", command=ventana.destroy)
boton_cerrar.pack()

# Mostramos la ventana
ventana.mainloop()


import tkinter as tk

ventana = tk.Tk()

# Creamos una etiqueta para mostrar una instrucción al usuario
etiqueta = tk.Label(ventana, text="Ingrese su nombre:")
etiqueta.pack()

# Creamos una entrada de texto para que el usuario ingrese su nombre
entrada_nombre = tk.Entry(ventana)
entrada_nombre.pack()

# Función que se ejecuta cuando el usuario hace clic en el botón
def mostrar_nombre():
    nombre = entrada_nombre.get()
    print("El nombre ingresado es:", nombre)

# Creamos un botón para que el usuario envíe los datos
boton_enviar = tk.Button(ventana, text="Enviar", command=mostrar_nombre)
boton_enviar.pack()

ventana.mainloop()