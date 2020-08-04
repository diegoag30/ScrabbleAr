import json
import os.path

class Partida():
    """Clase que maneja los datos de una partida guardada """
    def __init__(self,tiempo,atril_jugador,atril_ia, fichas_bolsa,filepath="save.json"):
        self._filepath = filepath
        self._tiempo = tiempo
        self._atril_jugador = atril_jugador
        self._atril_ia = atril_ia
        self._fichas_bolsa = fichas_bolsa


    def guardar_partida(self):
        """ Escribe en un archivo los datos de la partida actual."""
        try:
            file = open(self._filepath,"w")
            detalles_partida = {
                "tiempo": self._tiempo,
                "atril_jugador": self._atril_jugador,
                "atril_ia": self._atril_ia,
                "fichas_bolsa": self._fichas_bolsa,
            }
            json.dump(detalles_partida,file,indent=4)
            file.close()
        except:
            print("no se pudo guardar la partida")

    def retomar_partida(self):
        """ Verifica si existe una partida guardada, caso contrario devuelve un diccionario vacio"""
        data = {}
        try:
            #Si el archivo existe
            with open(self._filepath,"r") as file:
                data = json.load(file)
        except FileNotFoundError:
            print("el archivo no existe")
        except:
            print("Se produjo otro error")
        finally:
            return data

    def borrar_partida(self):
        try:
            os.remove(self._filepath)
        except FileNotFoundError:
            print("el archivo no existe")
        except:
            print("Se produjo otro error")






#partida = Partida(500,[1,2,3,4,5,6],[3,5,7,8,9],20)
#partida.borrar_partida()
#partida.guardar_partida()
