import PySimpleGUI as sg
# Clase que define el tablero y sus propiedades

class Cuadrado:
    def __init__(self, fila, columna,valor=0):
        self.fila = fila
        self.columna = columna
        self.valor = valor
        self.letra = None
    

class Tablero():

    def __init__(self):
        self.filas = 15
        self.columnas = 15
        self.tablero = []
        for fila in range(self.filas):
            self.tablero.append([])
            for columna in range(self.columnas):
                self.tablero[fila].append(Cuadrado(fila,columna))

    
