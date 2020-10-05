import PySimpleGUI as sg
from Configuracion import Configuracion


class Bolsa():
    def __init__(self,fichas):
        self._fichas = fichas
        self._bolsa_vacia = False
        self._layout = self.crear_ui()

    def get_layout(self):
        return self._layout

    def get_fichas(self):
        return self._fichas

    def bolsa_vacia(self):
        return self._bolsa_vacia

    def quitar_fichas(self,ficha,cantidad):
        cant_fichas = self._fichas[ficha]["cant"] - cantidad 
        if cant_fichas >=0:
            self._fichas[ficha]["cant"] = cant_fichas
        self.check_bolsa_vacia()

    def check_bolsa_vacia(self):
        """Metodo que sirve para chequear si la bolsa esta vacia """
        hay_fichas = False
        for values in self._fichas.values():
            #print(values["cant"])
            if values["cant"] > 0:
                hay_fichas = True
                break
        self._bolsa_vacia = not hay_fichas
        #print(self._bolsa_vacia)

    def crear_ui(self):
        """Crea la ui que tendra la bolsa """
        col_1 = []
        col_2 = []
        for i,(letra,datos) in enumerate(self._fichas.items()):
            if (i % 2 == 0):
                col_1.append([sg.Text(letra + ":"),sg.Text(datos["cant"],key=letra)])
            else:
                col_2.append([sg.Text(letra+ ":"),sg.Text(datos["cant"],key=letra)])
        layout = [
            [sg.Text("Bolsa",justification='center')],[sg.Column(col_1, element_justification='center'),sg.Column(col_2, element_justification='center')]
        ]
        return layout

    def letras_validas(self):
        """Devuelve un diccionario, que saca las fichas que tengan como cantidad 0 """
        nuevas_fichas = dict(self._fichas)
        for key,value in self._fichas.items():
            if value["cant"] == 0:
                try:
                    del nuevas_fichas[key]
                except KeyError:
                    print("No existe ese elemento en este diccionario")
        return nuevas_fichas

    def cant_letras(self,letra):
        if letra in self._fichas.keys():
            return self._fichas[letra]["cant"]

    def calcular_puntos(self,palabra):
        puntaje = 0
        for letra in palabra:
            puntaje = puntaje + self.get_fichas()[letra]["val"]
        return puntaje
            



conf = Configuracion()
bolsa = Bolsa(conf.getConfiguracionLetras())
print(bolsa.calcular_puntos("HOLA"))

