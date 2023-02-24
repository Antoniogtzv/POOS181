#1. Importar la clase
from personaje import *

#2. Solicitar atributos para el objeto
print("")
print("### Solicitud de datos Heroe ###")
espH = input("Escribe la especie del héroe: ")
nomH = input("Escribe el nombre del héroe: ")
altH = float(input("Escribe la altura del héroe: "))
cargaH = int(input("¿Cuántas balas se puede recargar?: "))

print("")
print("### Solicitud de datos Villano ###")
espV = input("Escribe la especie del villano: ")
nomV = input("Escribe el nombre del villano: ")
altV = float(input("Escribe la altura del villano: "))
cargaV = int(input("¿Cuántas balas se puede recargar?: "))

#3. Creamos dos objetos
Heroe = Personaje(espH, nomH, altH)
Villano = Personaje(espV, nomV, altV)

#4. Acceder a sus atributos
print("")
print("## Atributos y métodos del héroe ##")
print("El personaje pertenece a la raza: " + Heroe.especie)
print("Se llama: " + Heroe.nombre)
print("Mide: " + str(Heroe.altura) + " metros")
Heroe.correr(True)
Heroe.lanzarGranada()
Heroe.recargarArma(cargaH)
print("")

print("")
print("## Atributos y métodos del Villano ##")
print("El personaje pertenece a la raza: " + Villano.especie)
print("Se llama: " + Villano.nombre)
print("Mide: " + str(Villano.altura) + "  metros")
Villano.correr(False)
Villano.lanzarGranada()
Villano.recargarArma(cargaV)
print("")
