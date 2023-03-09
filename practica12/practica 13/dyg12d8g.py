import random
import string
import tkinter as tk

class PasswordGeneratorGUI:
    def __init__(self, master):
        self.master = master
        master.title("Generador de contraseñas")

        # Crear widgets
        self.label = tk.Label(master, text="Longitud de la contraseña:")
        self.label.pack()

        self.entry = tk.Entry(master)
        self.entry.insert(0, "8") # Valor por defecto
        self.entry.pack()

        self.button = tk.Button(master, text="Generar contraseña", command=self.generate_password)
        self.button.pack()

        self.password_label = tk.Label(master, text="")
        self.password_label.pack()

    def generate_password(self):
        length = int(self.entry.get())
        chars = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(chars) for i in range(length))
        self.password_label.configure(text=password)

root = tk.Tk()
gui = PasswordGeneratorGUI(root)
root.mainloop()