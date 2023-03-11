import tkinter as tk

class BancoApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Crear las variables de control para los widgets
        self.usuario_var = tk.StringVar()
        self.contrasena_var = tk.StringVar()
        self.saldo_var = tk.DoubleVar()
        
        # Configurar la ventana
        self.title("Banco App")
        self.geometry("300x200")
        
        # Crear los widgets de la ventana
        tk.Label(self, text="Nombre de usuario:").grid(row=0, column=0, padx=5, pady=5)
        self.usuario_entry = tk.Entry(self, textvariable=self.usuario_var)
        self.usuario_entry.grid(row=0, column=1, padx=5, pady=5)
        
        tk.Label(self, text="Contraseña:").grid(row=1, column=0, padx=5, pady=5)
        self.contrasena_entry = tk.Entry(self, textvariable=self.contrasena_var, show="*")
        self.contrasena_entry.grid(row=1, column=1, padx=5, pady=5)
        
        self.login_button = tk.Button(self, text="Iniciar sesión", command=self.iniciar_sesion)
        self.login_button.grid(row=2, column=0, padx=5, pady=5)
        
        self.saldo_label = tk.Label(self, textvariable=self.saldo_var)
        self.saldo_label.grid(row=3, column=0, columnspan=2, padx=5, pady=5)
        
        self.depositar_button = tk.Button(self, text="Depositar", command=self.depositar)
        self.depositar_button.grid(row=4, column=0, padx=5, pady=5)
        
        self.retirar_button = tk.Button(self, text="Retirar", command=self.retirar)
        self.retirar_button.grid(row=4, column=1, padx=5, pady=5)
        
        # Configurar la cuenta bancaria
        self.saldo = 1000.0
        
    def iniciar_sesion(self):
        usuario = self.usuario_var.get()
        contrasena = self.contrasena_var.get()
        
        # Verificar el nombre de usuario y la contraseña
        if usuario == "admin" and contrasena == "1234":
            self.actualizar_saldo()
        else:
            tk.messagebox.showerror("Error", "Nombre de usuario o contraseña incorrectos")
    
    def actualizar_saldo(self):
        self.saldo_var.set(f"Saldo: ${self.saldo:.2f}")
        
    def depositar(self):
        cantidad = float(tk.simpledialog.askstring("Depositar", "¿Cuánto dinero quieres depositar?"))
        self.saldo += cantidad
        self.actualizar_saldo()
        
    def retirar(self):
        cantidad = float(tk.simpledialog.askstring("Retirar", "¿Cuánto dinero quieres retirar?"))
        if cantidad > self.saldo:
            tk.messagebox.showerror("Error", "No tienes suficiente saldo para retirar esa cantidad")
        else:
            self.saldo -= cantidad
            self.actualizar_saldo()
        
if __name__ == "__main__":
    app = BancoApp()
    app.mainloop()