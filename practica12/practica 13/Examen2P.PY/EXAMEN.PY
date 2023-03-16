from tkinter import Tk,Frame,Button,messagebox


ventana= Tk()
ventana.title("Examen 2do parcial")
ventana.geometry("600x400")


class Estudiante:
    def __init__(self, nombre, apellido_paterno, apellido_materno, anio_nacimiento, carrera, anio_encurso,aleartorio):
        self.nombre = nombre
        self.apellido_paterno = apellido_paterno
        self.apellido_materno = apellido_materno
        self.anio_nacimiento = anio_nacimiento
        self.anio_curso = anio_encurso
        self.carrera = carrera
        self.aleartorio = aleartorio

class Generador:
    def __init__(self):
        self.root.title('Generador de matricula')
        self.nombre_label = Tk.Label(self.root, text='Nombre:')
        self.nombre_label.pack()
        self.nombre_entry = Tk.Entry(self.root)
        self.nombre_entry.pack

ventana.mainloop ()



