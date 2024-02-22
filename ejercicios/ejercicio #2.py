# Cree una clase Punto que represente un punto en el plano cartesiano.
# A la clase del punto anterior, defínale los siguientes métodos:
# - Un método mostrar que imprima por consola las coordenadas del punto
# - Un método mover que cambie las coordenadas del punto
# - Un método calcular_distancia que calcule la distancia de la instancia actual con otro punto.

class Punto:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def mostrar(self):
        print(f"La coordenada X es {self.x}"
              f" y La coordenada Y es {self.y}")

    def mover(self, nuevo_x, nuevo_y):
        self.x = nuevo_x
        self.y = nuevo_y

    def Calcular_distacia(self, otro_punto):
        distancia = ((self.x, otro_punto)**2 + (self.y, otro_punto)**2)


punto = Punto(x=5, y=2)
punto.mostrar()





