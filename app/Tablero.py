import PySimpleGUI as sg
import random

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
        self.filas = 15
        self.columnas = 15
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

    def change_valor(self,fila,columna,valor):
        self.tablero[fila][columna].valor = valor

    # Imprime los valores del tablero 1 por 1(en su mayoria seran espacios en blanco)
    def imprimir_tablero(self):
        for i in self.tablero:
            for j in i:
                print ("|",j.fila,j.columna,"|","valor: ",j.valor,"|")
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

    
    def comenzar(self,numero):
        #Se inicializa el tablero vacio
        self.iniciar_tablero()

        #Inicializa el tabler numero 1
        def tab1():
            #Valores que duplican
            self.change_valor(1,1,2)
            self.change_valor(2,2,2)
            self.change_valor(3,3,2)
            self.change_valor(4,4,2)
            self.change_valor(10,10,2)
            self.change_valor(11,11,2)
            self.change_valor(12,12,2)
            self.change_valor(13,13,2)
            self.change_valor(1,13,2)
            self.change_valor(2,12,2)
            self.change_valor(3,11,2)
            self.change_valor(4,10,2)
            self.change_valor(10,4,2)
            self.change_valor(11,3,2)
            self.change_valor(12,2,2)
            self.change_valor(13,1,2)

            #Valor del centro
            self.change_valor(7,7,0)

            #Valores que triplican
            self.change_valor(0,0,3)
            self.change_valor(0,7,3)
            self.change_valor(0,14,3)
            self.change_valor(14,7,3)
            self.change_valor(14,14,3)
            self.change_valor(7,14,3)
            self.change_valor(7,0,3)
            self.change_valor(14,0,3)



        #Inicializa el tablero numero 2    
        def tab2():
            #Valores que duplican
            self.change_valor(1,7,2)
            self.change_valor(2,6,2)
            self.change_valor(3,5,2)
            self.change_valor(4,4,2)
            self.change_valor(5,3,2)
            self.change_valor(6,2,2)
            self.change_valor(7,1,2)
            self.change_valor(8,2,2)
            self.change_valor(9,3,2)
            self.change_valor(10,4,2)
            self.change_valor(11,5,2)
            self.change_valor(12,6,2)
            self.change_valor(13,7,2)
            self.change_valor(2,8,2)
            self.change_valor(3,9,2)
            self.change_valor(4,10,2)
            self.change_valor(5,11,2)
            self.change_valor(6,12,2)
            self.change_valor(7,13,2)
            self.change_valor(8,12,2)
            self.change_valor(9,11,2)
            self.change_valor(10,10,2)
            self.change_valor(11,9,2)
            self.change_valor(12,8,2)

            #Valor del centro
            self.change_valor(7,7,0)

            #Valores que triplican
            self.change_valor(4,7,3)
            self.change_valor(5,6,3)
            self.change_valor(6,5,3)
            self.change_valor(7,4,3)
            self.change_valor(8,5,3)
            self.change_valor(9,6,3)
            self.change_valor(10,7,3)
            self.change_valor(9,8,3)
            self.change_valor(8,9,3)
            self.change_valor(7,10,3)
            self.change_valor(6,9,3)
            self.change_valor(5,8,3)

        #Inicializa el tabler numero 3  //FALTA IMPLEMENTAR
        def tab3():
            return "tablero 3"

        #Sirve para seleccionar el tipo de tablero
        switcher = {
            1: tab1,
            2: tab2,
            3: tab3,
        }
        # Obtiene la funcion del diccionario
        func = switcher.get(numero, lambda: "Numero invalido")
        # Ejecuta la funcion
        print (func())

