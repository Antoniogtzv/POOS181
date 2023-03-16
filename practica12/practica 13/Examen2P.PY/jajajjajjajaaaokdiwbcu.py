ventana = tk.Tk()

etiqueta = tk.Label(ventana, text="Ingrese su nombre:")
etiqueta.pack()

# Creamos una entrada de texto para que el usuario ingrese su nombre
entrada_nombre = tk.Entry(ventana)
entrada_nombre.pack()
entrada_app.pack = tk.Entry(ventana)
entrada_nombre.pack()



def mostrar_nombre():
    nombre = entrada_nombre.get()
    print("El nombre ingresado es:", nombre)

# Creamos un botón para que el usuario envíe los datos
boton_enviar = tk.Button(ventana, text="Enviar", command=mostrar_nombre)
boton_enviar.pack()

ventana.mainloop()