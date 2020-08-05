import json
import os.path
import PySimpleGUI as sg
import time


class Puntaje():
    """ Clase que maneja el ranking"""
    def __init__(self,filepath="ranking.json"):
        self._filepath = filepath
        self._top10 = []
        self._color_ventana = '#00796B'

    @property #getter filepath
    def filepath(self):
        return self._filepath

    @filepath.setter #Propiedad SETTER
    def filepath(self, filepath):
        print ("Modificando nombre..")
        self._filepath = filepath

    @filepath.deleter #Propiedad DELETER
    def filepath(self): 
        print("Borrando nombre..")
        del self._filepath

    def create_file(self):
        """ Verifica la existencia del archivo, si existe lee los puntajes y los guarda en _top10,
        caso contrario creara el archivo. Para cualquiera de los dos casos devuelve _top10 """
        try:
            #Si el archivo existe
            file = open(self._filepath,"r")
            data = json.load(file)
            #print(data)
            self._top10 = data
            file.close()
        except:
            #Si el archivo no existe
            print("Creando archivo")
            file = open(self._filepath,"x")
            file.close()
        finally:
            return self._top10


    def agregar_nuevo_puntaje(self,jugador,cant_puntos,nivel):
        """Agrega al archivo el jugador con sus datos correspondientes """
        # Se crea el archivo, o se leen los datos anteriores
        puntajes = self.create_file()
        horario_Actual = time.localtime()
        fecha_actual = time.strftime("%m/%d/%Y")
        if(len(puntajes) < 10):
            try:
                file = open(self._filepath,"w")
                puntaje = {
                    "jugador": jugador,
                    "fecha": fecha_actual,
                    "puntaje": cant_puntos,
                    "nivel": nivel,
                }
                puntajes.append(puntaje)
                puntajes = sorted(puntajes, key = lambda i: i["puntaje"], reverse = True)
                json.dump(puntajes,file,indent=4)
                file.close()
            except:
                print("El usuario no cuenta con permisos de escritura")
        else:
            try:
                file = open(self._filepath,"w")
                puntaje = {
                    "jugador":jugador,
                    "fecha":fecha_actual,
                    "puntaje": cant_puntos,
                    "nivel": nivel,
                }
                puntajes[-1] = puntaje
                puntajes = sorted(puntajes, key = lambda i: i["puntaje"], reverse = True)
                json.dump(puntajes,file,indent=4)
                file.close()
            except:
                print("El usuario no cuenta con permisos de escritura 2")  
          
    def create_ui(self):
        ''' Crea la UI de los puntajes.'''

        ##Se obtienen los puntajes
        puntajes = self.create_file()

        ### Instanciacion de las columnas
        col_nombre = [
            [sg.Text("NOMBRE",background_color= self._color_ventana)]
        ]
        col_puntaje = [
            [sg.Text("PUNTAJE",background_color= self._color_ventana)]
        ]
        col_nivel = [
            [sg.Text("NIVEL",background_color= self._color_ventana)]
        ]
        col_fecha = [
            [sg.Text("FECHA",background_color= self._color_ventana)]
        ]

        ##Se agrega de forma dinamica los datos correspondientes a cada columna
        for p in puntajes:
            col_nombre.append([sg.Text(p["jugador"],background_color= self._color_ventana)])
            col_puntaje.append([sg.Text(str(p["puntaje"]),background_color= self._color_ventana)])
            col_nivel.append([sg.Text(p["nivel"],background_color= self._color_ventana)])
            col_fecha.append([sg.Text(p["fecha"],background_color= self._color_ventana)])
        layout = [[sg.Column(col_nombre, element_justification='center'),sg.Column(col_puntaje, element_justification='center')
        ,sg.Column(col_nivel, element_justification='center'),sg.Column(col_fecha, element_justification='center')]]

        ## Configuracion de la ventana, y eventos
        window = sg.Window('Top 10 mejores puntajes', layout)
        while True:             
            event, values = window.read()
            if event in (sg.WIN_CLOSED, 'Cancel'):
                break
        window.close()


p = Puntaje()
#p.create_file()
p.agregar_nuevo_puntaje("diego",10000,"dificil")



