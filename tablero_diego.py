import PySimpleGUI as sg
import random

class Cuadrado:
    def __init__(self, fila, columna,valor=0):
        self.fila = fila
        self.columna = columna
        self.valor = valor
    

class Tablero():

    def __init__(self):
        filas = columnas = 15
        colors = ["white","red","blue"]
        self.tablero = []
        for fila in range(filas):
            self.tablero.append([])
            for columna in range(columnas):
                self.tablero[fila].append(Cuadrado(fila,columna))
        self.layout = [[sg.Button('', button_color=("black",random.choice(colors)) ,size=(4, 2), key=(i,j), pad=(0,0)) for j in range(columnas)] for i in range(filas)]
        self.window = sg.Window('Scrabble.ar', self.layout)

    
