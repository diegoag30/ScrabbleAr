import json
import os.path

class Puntaje():
    """ Clase que maneja el ranking"""
    def __init__(self,filepath="ranking.json"):
        self._filepath = filepath
        self._top10 = []

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


    def agregar_nuevo_puntaje(self,jugador,cant_puntos,fecha,nivel):
        """Agrega al archivo el jugador con sus datos correspondientes """
        # Se crea el archivo, o se leen los datos anteriores
        puntajes = self.create_file()
        if(len(puntajes) < 10):
            try:
                file = open(self._filepath,"w")
                puntaje = {
                    "jugador": jugador,
                    "fecha": fecha,
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
                    "fecha":fecha,
                    "puntaje": cant_puntos,
                    "nivel": nivel,
                }
                puntajes[-1] = puntaje
                puntajes = sorted(puntajes, key = lambda i: i["puntaje"], reverse = True)
                json.dump(puntajes,file,indent=4)
                file.close()
            except:
                print("El usuario no cuenta con permisos de escritura 2")            


p = Puntaje()
#p.create_file()
p.agregar_nuevo_puntaje("diego",20,"14/07/2020","dificil")