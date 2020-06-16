import PySimpleGUI as sg
from Configuracion import Configuracion
from main import main_game



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
    event, values = window.read()
    print(event, values)
    if event == sg.WIN_CLOSED:
        break
    if event == 'LOGO':
        window.close(); del window
        main_game()
    if event == 'CONFIGURACION':
        window.close(); del window
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
                sg.Popup('¡EN PROCESO!', icon='ScrabbleGO.ico')
                # event, values = window.read()
                # print(event, values)
                break
    break