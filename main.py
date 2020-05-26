from tablero_diego import Tablero

tablero = Tablero()
while True:
    event,values = tablero.window().read()
    if event in (None, 'Exit'):
        break
tablero.window.close()