# Cree una clase Carta que contenga dos propiedades valor y pinta,
# las cuales son asignadas solo al momento de la construcción del objeto
# (se pasan como parámetros en el constructor).
# Defina 4 constantes que representan los nombres de las 4 pintas que puede tener una carta.

class Carta:

    def __init__(self, pinta, valor):
        self.pinta = pinta
        self.valor = valor


Pinta_Corazon = "Corazon"
Pinta_Diamante = "Dimanate"
Pinta_Trebol = "Trebol"
Pinta_Pica = "Pica"

