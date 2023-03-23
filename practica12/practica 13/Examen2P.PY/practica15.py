import tkinter as tk

# Crear la ventana principal
root = tk.Tk()

# Crear las variables de entrada
name_var = tk.StringVar()
password_var = tk.StringVar()
email_var = tk.StringVar()

# Función para guardar los datos del usuario
def save_user():
    name = name_var.get()
    password = password_var.get()
    email = email_var.get()
    user_data = [name, password, email]
    print("Usuario guardado:", user_data)

# Crear las etiquetas y campos de entrada
name_label = tk.Label(root, text="Nombre:")
name_entry = tk.Entry(root, textvariable=name_var)
password_label = tk.Label(root, text="Contraseña:")
password_entry = tk.Entry(root, textvariable=password_var, show="*")
email_label = tk.Label(root, text="Correo electrónico:")
email_entry = tk.Entry(root, textvariable=email_var)
save_button = tk.Button(root, text="Guardar usuario", command=save_user)

# Colocar los elementos en la ventana
name_label.grid(row=0, column=0)
name_entry.grid(row=0, column=1)
password_label.grid(row=1, column=0)
password_entry.grid(row=1, column=1)
email_label.grid(row=2, column=0)
email_entry.grid(row=2, column=1)
save_button.grid(row=3, column=1)

# Iniciar la ventana
root.mainloop()