import PySimpleGUI as sg
import random
from src.Tablero import *
# Maneja la UI del juego

colors = ["white","red","blue"]
tablero = Tablero()
layout = [[sg.Button('', button_color=("black",random.choice(colors)) ,size=(4, 2), key=(i,j), pad=(0,0)) for j in range(tablero.columnas)] for i in range(tablero.filas)]
window = sg.Window('Scrabble.ar', layout)
