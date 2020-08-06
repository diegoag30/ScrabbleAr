import PySimpleGUI as sg
from Configuracion import Configuracion
from main3 import main_game
import configuracion_letras
from puntajes import Puntaje

#Puntaje instanciado
mejores_puntajes = Puntaje()
#funcion para cambiar el background del programa a un color personalizado
sg.theme_background_color(color='#00796B')

conf = Configuracion()
window = conf.ventanaPrincipal()

# _configuraciones_seleccionadas = {
#             'tiempo':'',
#             'dificultad':'',
#             'tablero':1
#             }      

letras = {}

while True:
    event, values = window.read()
    print(event, values)
    if event == sg.WIN_CLOSED:
        break
    if event == 'RANKING':
        mejores_puntajes.create_ui()
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
                letras = conf.getConfiguracionLetras()
                print(letras)
                if event == 'Aplicar':
                    print('cambios realizados')

                    # for letra in letras:
                    #     print(letra,' ---> ',letras[letra]['cant'], ' ', letras[letra]['val'])

                    #modifico la cantidad de letras en base a lo ingresado en el input del menu de configurar letras
                    letras['A']['cant']=values['cantA']
                    letras['B']['cant']=values['cantB']
                    letras['C']['cant']=values['cantC']
                    letras['D']['cant']=values['cantD']
                    letras['E']['cant']=values['cantE']
                    letras['F']['cant']=values['cantF']
                    letras['G']['cant']=values['cantG']
                    letras['H']['cant']=values['cantH']
                    letras['I']['cant']=values['cantI']
                    letras['J']['cant']=values['cantJ']
                    letras['K']['cant']=values['cantK']
                    letras['L']['cant']=values['cantL']
                    letras['M']['cant']=values['cantM']
                    letras['N']['cant']=values['cantN']
                    letras['O']['cant']=values['cantO']
                    letras['P']['cant']=values['cantP']
                    letras['Q']['cant']=values['cantQ']
                    letras['R']['cant']=values['cantR']
                    letras['S']['cant']=values['cantS']
                    letras['T']['cant']=values['cantT']
                    letras['U']['cant']=values['cantU']
                    letras['V']['cant']=values['cantV']
                    letras['W']['cant']=values['cantW']
                    letras['X']['cant']=values['cantX']
                    letras['Y']['cant']=values['cantY']
                    letras['Z']['cant']=values['cantZ']

                    #modifico el valor del puntaje de las letras en base a lo ingresado en el input del menu de configurar letras
                    letras['A']['val']=values['valA']
                    letras['B']['val']=values['valB']
                    letras['C']['val']=values['valC']
                    letras['D']['val']=values['valD']
                    letras['E']['val']=values['valE']
                    letras['F']['val']=values['valF']
                    letras['G']['val']=values['valG']
                    letras['H']['val']=values['valH']
                    letras['I']['val']=values['valI']
                    letras['J']['val']=values['valJ']
                    letras['K']['val']=values['valK']
                    letras['L']['val']=values['valL']
                    letras['M']['val']=values['valM']
                    letras['N']['val']=values['valN']
                    letras['O']['val']=values['valO']
                    letras['P']['val']=values['valP']
                    letras['Q']['val']=values['valQ']
                    letras['R']['val']=values['valR']
                    letras['S']['val']=values['valS']
                    letras['T']['val']=values['valT']
                    letras['U']['val']=values['valU']
                    letras['V']['val']=values['valV']
                    letras['W']['val']=values['valW']
                    letras['X']['val']=values['valX']
                    letras['Y']['val']=values['valY']
                    letras['Z']['val']=values['valZ']

                    # for letra in letras:
                    #     print(letra,' ---> ',letras[letra]['cant'], ' ', letras[letra]['val'])

                    print(letras)
                    conf.setConfiguracionLetras(letras)
                    menu_configuracion_de_letras.close()
                if event == 'Salir':
                    menu_configuracion_de_letras.close()