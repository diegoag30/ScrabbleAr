import PySimpleGUI as sg
# Clase que define el tablero y sus propiedades

class Cuadrado:
    def __init__(self, fila, columna,letra='',valor = 0):
        self.fila = fila
        self.columna = columna
        self._letra = letra
        self.__valor = valor


    @property
    def letra(self):
        return self._letra

    @letra.setter
    def letra(self,letra):
        self._letra = letra


    @property
    def valor(self):
        return self._valor 
          
    @valor.setter
    def valor(self,valor):
        self._valor = valor


    


class Tablero():

    def __init__(self):
        self.filas = 10
        self.columnas = 10
        self.tablero = []


    def iniciar_tablero(self):
        for fila in range(self.filas):
            row = []
            for columna in range(self.columnas):
                row.append(Cuadrado(fila,columna))
            self.tablero.append(row)


                
    def change_letra(self,fila,columna,letra):
        self.tablero[fila][columna].letra = letra
        print (self.tablero[fila][columna].letra)


    
