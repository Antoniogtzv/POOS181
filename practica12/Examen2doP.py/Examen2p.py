import tkinter as tk

# Función que se ejecuta cuando se hace clic en el botón "Imprimir"
def imprimir():
    # Obtener los valores ingresados por el usuario
    nombre = entry_nombre.get()
    apellidos = entry_apellidos.get()
    anio_nacimiento = int(entry_anio_nacimiento.get())
    anio_actual = int(entry_anio_actual.get())
    carrera = entry_carrera.get()
    numero_aleatorio = int(entry_numero_aleatorio.get())

    # Calcular los primeros dos dígitos del año de nacimiento
    anio_nacimiento_dos_digitos = str(anio_nacimiento)[:2]

    # Imprimir los resultados
    print("Nombre: ", nombre)
    print("Apellidos: ", apellidos)
    print("Año de nacimiento (2 primeros dígitos): ", anio_nacimiento_dos_digitos)
    print("Carrera: ", carrera)
    print("Número aleatorio (2 primeros dígitos): ", str(numero_aleatorio)[:2])

# Crear la ventana principal
ventana = tk.Tk()

# Crear los widgets de entrada
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

label_numero_aleatorio = tk.Label(ventana, text="Número aleatorio:")
entry_numero_aleatorio = tk.Entry(ventana)

# Crear el botón "Imprimir"
boton_imprimir = tk.Button(ventana, text="Imprimir", command=imprimir)

# Ubicar los widgets en la ventana
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

label_numero_aleatorio.grid(row=5, column=0)
entry_numero_aleatorio.grid(row=5, column=1)

boton_imprimir.grid(row=6, column=1)

# Iniciar la ventana
ventana.mainloop()
