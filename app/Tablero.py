import PySimpleGUI as sg

# La clase cuadrado esta compuesta por sus coordenadas(fila,columna), la letra que contiene(se inicializa en blanco), y el valor que viene a ser
# un multiplicador para cuando se necesite calcular el puntaje.
class Cuadrado:
    def __init__(self, fila, columna,letra=' ',valor = 1):
        self.fila = fila
        self.columna = columna
        self._letra = letra
        self._valor = valor


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


    

# La clase tablero se encarga de generar una matriz de objetos de la clase cuadrado, se inicializa con espacios en blanco, que luego pueden ser modificados
class Tablero():

    def __init__(self):
        self.filas = 10
        self.columnas = 10
        self._tablero = []

    @property
    def tablero(self):
        return self._tablero

    @tablero.setter
    def tablero(self,tablero):
        self._tablero = tablero


    def iniciar_tablero(self):
        for fila in range(self.filas):
            row = []
            for columna in range(self.columnas):
                row.append(Cuadrado(fila,columna))
            self.tablero.append(row)


    #Cambia la letra de un cuadrado del tablero, indicando la fila y columna donde se encuentra el cuadrado, y ademas el valor de la letra     
    def change_letra(self,fila,columna,letra):
        self.tablero[fila][columna].letra = letra

    # Imprime los valores del tablero 1 por 1(en su mayoria seran espacios en blanco)
    def imprimir_tablero(self):
        for fila in self.tablero:
            for columna in fila:
                print (columna.letra)
            print

    #Obtiene una lista de las palabras que hayan sido colocadas en cada fila, si hay un espacio entre letras, este va incluido
    def get_word(self):
        res = ""
        words = []
        for fila in self._tablero:
            for columna in fila:
                res = res + columna.letra
            res = res.strip()
            if(res != ""):
                words.append(res)
            res = ""
        print(words)
        return words



    
