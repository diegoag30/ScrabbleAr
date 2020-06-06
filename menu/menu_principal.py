import PySimpleGUI as sg
from Configuracion import Configuracion

#funcion para cambiar el background del programa a un color personalizado
sg.theme_background_color(color='#00796B')

conf = Configuracion()
window = conf.ventanaPrincipal()


while True:
    event, values = window.read()
    print(event, values)
    if event == sg.WIN_CLOSED:
        break
    if event == 'CONFIGURACION':
        window.close(); del window
        # window = sg.Window('Scrabble GO - Configuracion', menu, icon='ScrabbleGO.ico', size=(1302,800))
        ventana_configuracion = conf.menuConfiguracion()
        event, values = ventana_configuracion.read()
        print(event, values)
        if event == 'SIGUIENTE':
            sg.Popup('¡EN PROCESO!', icon='ScrabbleGO.ico')
            event, values = ventana_configuracion.read()
            print(event, values)