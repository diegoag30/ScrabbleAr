import PySimpleGUI as sg
from Configuracion import Configuracion
from main3 import main_game
import configuracion_letras



#funcion para cambiar el background del programa a un color personalizado
sg.theme_background_color(color='#00796B')

conf = Configuracion()
window = conf.ventanaPrincipal()

# _configuraciones_seleccionadas = {
#             'tiempo':'',
#             'dificultad':'',
#             'tablero':1
#             }      


while True:
    print("pase por aqui")
    event, values = window.read()
    print(event, values)
    if event == sg.WIN_CLOSED:
        break
    if event == 'LOGO':
        window.close(); del window

        main_game(conf.get_tablero_elegido())
    if event == 'CONFIGURACION':
        window.Disappear()
        # window = sg.Window('Scrabble GO - Configuracion', menu, icon='ScrabbleGO.ico', size=(1302,800))
        # window = conf.menuConfiguracion()
        ventana_configuracion = conf.menuConfiguracion()
        while True:
            event, values = ventana_configuracion.read()
            print(event, values)
            if event == sg.WIN_CLOSED:
                break
            conf.setConfiguracionesSeleccionadas(event)
            print(conf.getConfiguracionesSeleccionadas())

            if event == 'SIGUIENTE':
                # print(conf.getConfiguracionesSeleccionadas())
                # event, values = window.read()
                # print(event, values)
                ventana_configuracion.close()
                window.reappear()
                break
            if event == 'Configurar letras':
                menu_configuracion_de_letras = configuracion_letras.GUI_configuracion_de_letras()
                event, values = menu_configuracion_de_letras.read()
            if event == 'Aplicar':
                print('cambios realizados')
                menu_configuracion_de_letras.close()
            if event == 'Salir':
                menu_configuracion_de_letras.close()