import tkinter as tk
from tkinter import messagebox

def login():
    email = email_entry.get()
    password = password_entry.get()

    # Comprobar si el usuario y la contraseña son correctos
    if email == "antonioguvi0419@gmail.com" and password == "contraseña":
        messagebox.showinfo("Inicio de sesión", "El usuario y contraseña son correctos. Bienvendio")
        root.destroy()
    else:
        messagebox.showerror("Error", "Usuario o contraseña incorrectos")
        password_entry.delete(0, tk.END)

root = tk.Tk()
root.title("Inicio de sesión")

email_label = tk.Label(root, text="Correo electrónico:")
email_label.grid(row=0, column=0, padx=5, pady=5)

email_entry = tk.Entry(root)
email_entry.grid(row=0, column=1, padx=5, pady=5)

password_label = tk.Label(root, text="Contraseña:")
password_label.grid(row=1, column=0, padx=5, pady=5)

password_entry = tk.Entry(root, show="*")
password_entry.grid(row=1, column=1, padx=5, pady=5)

login_button = tk.Button(root, text="Iniciar sesión", command=login)
login_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

root.mainloop()