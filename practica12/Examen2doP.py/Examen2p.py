import tkinter as tk
import random

class Estudiante:
    def __init__(self, nombre, apellido_paterno, apellido_materno, anio_nacimiento, carrera):
        self.nombre = nombre
        self.apellido_paterno = apellido_paterno
        self.apellido_materno = apellido_materno
        self.anio_nacimiento = anio_nacimiento
        self.carrera = carrera

    def generar_matricula(self):
        anio_actual = datetime.datetime.now().year % 100
        anio_nacimiento = self.anio_nacimiento % 100
        primera_letra_nombre = self.nombre[0]
        dos_letras_apellido_paterno = self.apellido_paterno[:2]
        dos_letras_apellido_materno = self.apellido_materno[:2]
        dos_digitos_aleatorios = '{:02d}'.format(random.randint(0, 99))
        tres_primeras_letras_carrera = self.carrera[:3]

        matricula = f'{anio_actual}{anio_nacimiento}{primera_letra_nombre}{dos_letras_apellido_paterno}{dos_letras_apellido_materno}{dos_digitos_aleatorios}{tres_primeras_letras_carrera}'

        return matricula

class MatriculaGenerator:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('Generador de matrícula')
        
        self.nombre_label = tk.Label(self.root, text='Nombre:')
        self.nombre_label.pack()
        self.nombre_entry = tk.Entry(self.root)
        self.nombre_entry.pack()

        self.apellido_paterno_label = tk.Label(self.root, text='Apellido Paterno:')
        self.apellido_paterno_label.pack()
        self.apellido_paterno_entry = tk.Entry(self.root)
        self.apellido_paterno_entry.pack()

        self.apellido_materno_label = tk.Label(self.root, text='Apellido Materno:')
        self.apellido_materno_label.pack()
        self.apellido_materno_entry = tk.Entry(self.root)
        self.apellido_materno_entry.pack()

        self.anio_nacimiento_label = tk.Label(self.root, text='Año de nacimiento:')
        self.anio_nacimiento_label.pack()
        self.anio_nacimiento_entry = tk.Entry(self.root)
        self.anio_nacimiento_entry.pack()

        self.carrera_label = tk.Label(self.root, text='Carrera:')
        self.carrera_label.pack()
        self.carrera_entry = tk.Entry(self.root)
        self.carrera_entry.pack()

        self.generar_matricula_button = tk.Button(self.root, text='Generar matrícula', command=self.generar_matricula)
        self.generar_matricula_button.pack()

        self.matricula_label = tk.Label(self.root, text='')
        self.matricula_label.pack()

    def generar_matricula(self):
        nombre = self.nombre_entry.get()
        apellido_paterno = self.apellido_paterno_entry.get()
        apellido_materno = self.apellido_materno_entry.get()
        anio_nacimiento = int(self.anio_nacimiento_entry.get())
        carrera = self.carrera_entry.get()

        estudiante = Estudiante(nombre, apellido_paterno, apellido_materno, anio_nacimiento, carrera)
        matricula = estudiante.generar_matricula()
        self.matricula_label.config(text=f'Su matrícula es: {matricula}')

    def start(self):
        self.root.mainloop()

if __name__ == '__main__':
    GeneratorExit