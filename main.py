from src.Tablero import Tablero
from ui.juego import *
# clase principal que llama a juego.py

while True:
    event,values = window.read()
    if event in (None, 'Exit'):
        break
window.close()