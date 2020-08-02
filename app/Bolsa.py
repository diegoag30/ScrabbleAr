import PySimpleGUI as sg

class Bolsa():
    def __init__(self,total):
        self._total = total
        self._fichas_restantes = total
        self._bolsa_vacia = False

    def get_fichas_restantes(self):
        return self._fichas_restantes
        
    def get_bolsa_vacia(self):
        return self._bolsa_vacia

    def set_bolsa_vacia(self,valor):
        self._bolsa_vacia = valor
    
    def sacar_fichas(self,fichas_repartidas):
        if (self._fichas_restantes - fichas_repartidas) >= 0:
            self._fichas_restantes -= fichas_repartidas
        else:
            self._fichas_restantes = 0    
            set_bolsa_vacia(True)
   



