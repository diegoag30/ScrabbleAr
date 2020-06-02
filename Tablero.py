import PySimpleGUI as sg
# Clase que define el tablero y sus propiedades

class Cuadrado:
    def __init__(self, fila, columna,valor=0):
        self.fila = fila
        self.columna = columna
        self.valor = valor
        self.letra = None

    def set_letra(self,valor):
        self.letra = valor

    def get_letra(self):
        return self.letra
    
    def set_valor(self,valor):
        self.valor = valor

    def get_valor(self):
        return self.valor
    

class Tablero():

    def __init__(self):
        self.filas = 10
        self.columnas = 10
        self.tablero = []


    def iniciar_tablero(self):
        for fila in range(self.filas):
            row = []
            for columna in range(self.columnas):
                cuadrado = Cuadrado(fila,columna)
                row.append(cuadrado)
            self.tablero.append(cuadrado)


                
    def change_letra(self,fila,columna):
        self.tablero[fila][columna].get_valor() #causa error


    
