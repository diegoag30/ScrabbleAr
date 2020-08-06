import PySimpleGUI as sg
from Configuracion import Configuracion
from maingame import main_game
import configuracion_letras
from puntajes import Puntaje

#Puntaje instanciado
mejores_puntajes = Puntaje()
#funcion para cambiar el background del programa a un color personalizado
sg.theme_background_color(color='#00796B')
conf = Configuracion()
window = conf.ventanaPrincipal()


# Design pattern 1 - First window does not remain active

layout = [[ sg.Text('Window 1'),],
          [sg.Input(do_not_clear=True)],
          [sg.Text(size=(15,1),  key='-OUTPUT-')],
          [sg.Button('Launch 2')]]
#================================== CREO EL LAYOUT PARA LA VENTANA INICIAL ==========================================================================
layout_ventana_principal = [
            [sg.Image(r'app/images/scrabble_logo508x214.png', size=(1000, 300), pad=((0,0),(200,0)), background_color='#00796B')],
            [sg.Button(button_color=(sg.theme_background_color(), sg.theme_background_color()), image_filename='app/images/play.png', image_size=(256, 256), key='JUGAR', image_subsample=2, border_width=0,pad=((110,0),(0,100))), 
            sg.Button(button_color=(sg.theme_background_color(), sg.theme_background_color()), image_filename='app/images/star.png', image_size=(256, 256), key='RANKING', image_subsample=2, border_width=0,pad=((0,0),(0,100))), 
            sg.Button(button_color=(sg.theme_background_color(), sg.theme_background_color()), image_filename='app/images/configuracion.png', image_size=(256, 256), key='CONFIGURACION', image_subsample=2, border_width=0,pad=((0,0),(0,100)))]
         ]


ventana_inicial = sg.Window('Scrabble GO', layout_ventana_principal, icon='ScrabbleGO.ico')
ventana_menu_configuracion_active=False
ventana_menu_letras_active=False
while True:
    ev_ventana_inicial, vals_ventana_inicial = ventana_inicial.read(timeout=100)
    if ev_ventana_inicial == sg.WIN_CLOSED:
        break
    # ventana_inicial.FindElement('-OUTPUT-').update(vals_ventana_inicial[0])
    if ev_ventana_inicial == 'JUGAR':
        ventana_inicial.close()
        main_game(conf.get_tablero_elegido())
    if ev_ventana_inicial == 'RANKING':
        mejores_puntajes.create_ui()
    if ev_ventana_inicial == 'CONFIGURACION'  and not ventana_menu_configuracion_active:
        ventana_menu_configuracion_active = True
        ventana_inicial.Hide()
        layout2 = [[sg.Text('Window 2')],       # note must create a layout from scratch every time. No reuse
                   [sg.Button('Exit')]]
#================================== CREO EL LAYOUT PARA LA VENTANA DE CONFIGURACION ==========================================================================
        layout_configuracion = [
            # [sg.Text('Tiempo de juego', background_color=color_de_fondo, text_color='white', font=('Helvetica', 15, 'bold'), pad=((446,0),(15,15)), tooltip=('Elije el tiempo que durara la partida'))],
            #--------------------SECCION TIEMPO DE JUEGO--------------------
            [sg.Image(r'app/images/tiempo_de_juego.png', tooltip=('Elige el tiempo que durara la partida'), size=(650, 50), pad=((200,0),(10,10)), background_color='#00796B')],
            [sg.Button(button_color=(sg.theme_background_color(), sg.theme_background_color()), image_filename='app/images/minimo_375x138.png', image_size=(170, 64), key='minimo', image_subsample=2, border_width=0,pad=((440,0),(0,0)), tooltip=('Elija esta opción si quiere jugar una partida rapida'))],
            [sg.Button(button_color=(sg.theme_background_color(), sg.theme_background_color()), image_filename='app/images/medio_375x138.png', image_size=(170, 64), key='medio', image_subsample=2, border_width=0,pad=((440,0),(0,0)), tooltip=('Elija esta opción si quiere jugar una partida normal'))],
            [sg.Button(button_color=(sg.theme_background_color(), sg.theme_background_color()), image_filename='app/images/maximo_375x138.png', image_size=(170, 64), key='maximo', image_subsample=2, border_width=0,pad=((440,0),(0,0)), tooltip=('Elija esta opción si quiere jugar una partida con mucho tiempo'))],
            # [sg.Text('Nivel de dificultad', background_color=color_de_fondo, text_color='white', font=('Helvetica', 15, 'bold'), pad=((441,0),(15,15)), tooltip=('En esta opción, se configurará el nivel del juego.'))],
            #--------------------SECCION NIVEL DE DIFICULTAD--------------------
            [sg.Image(r'app/images/nivel_de_dificultad.png', tooltip=('En esta opción, se configurará el nivel del juego.'), size=(650, 50), pad=((200,0),(10,10)), background_color='#00796B')],
            [sg.Button(button_color=(sg.theme_background_color(), sg.theme_background_color()), image_filename='app/images/facil_375x138.png', image_size=(170, 64), key='facil', image_subsample=2, border_width=0,pad=((440,0),(0,0)), tooltip=('Se jugara con cualquier tipo de palabra (adjetivos, sustantivos y verbos).'))],
            [sg.Button(button_color=(sg.theme_background_color(), sg.theme_background_color()), image_filename='app/images/normal_375x138.png', image_size=(170, 64), key='normal', image_subsample=2, border_width=0,pad=((440,0),(0,0)), tooltip=('Se jugara sólo con verbos y adjetivos.'))],
            [sg.Button(button_color=(sg.theme_background_color(), sg.theme_background_color()), image_filename='app/images/dificil_375x138.png', image_size=(170, 64), key='dificil', image_subsample=2, border_width=0,pad=((440,0),(0,0)), tooltip=('Se jugara con una categoría elegida al azar entre verbos y adjetivos.'))],
            # [sg.Text('Seleccionar Tablero', tooltip=('Elija entre uno de los tres tableros disponibles para jugar, por defecto se elije el tablero 1'), background_color=color_de_fondo, text_color='white', font=('Helvetica', 15, 'bold'), pad=((430,0),(15,15)))],
            #--------------------SECCION DE TABLERO--------------------
            [sg.Image(r'app/images/modelo_de_tablero.png', tooltip=('Elija entre uno de los tres tableros disponibles para jugar, por defecto se elije el tablero 1'), size=(650, 50), pad=((200,0),(10,10)), background_color='#00796B')],
            #para el diseño de los tableros uso imagenes por defecto hasta que se pueda visualizar los 3 tableros para realizar una miniatura
            [sg.Button(button_color=(sg.theme_background_color(), sg.theme_background_color()), image_filename='app/images/tablero_1.png', image_size=(171,171), key='tablero_1', image_subsample=3, border_width=0,pad=((218,0),(0,0)), tooltip=('Tablero dieñado por Cristian')),
            sg.Button(button_color=(sg.theme_background_color(), sg.theme_background_color()), image_filename='app/images/tablero_2.png', image_size=(171,171), key='tablero_2', image_subsample=3, border_width=0,pad=((50,0),(0,0)), tooltip=('Tablero dieñado por Diego')),
            sg.Button(button_color=(sg.theme_background_color(), sg.theme_background_color()), image_filename='app/images/tablero_3.png', image_size=(171,171), key='tablero_3', image_subsample=3, border_width=0,pad=((50,0),(0,0)), tooltip=('Tablero de ejemplo'))],
            [sg.Button('Configurar')],
            [sg.Button('SIGUIENTE')]
            ]

        ventana_menu_configuracion = sg.Window("Scrabble GO", layout_configuracion, icon='ScrabbleGO.ico', size=(1050,850))
        while True:
            ev_menu_configuracion, vals_menu_configuracion = ventana_menu_configuracion.read()
            print('EVENTOS - MENU CONFIGURACION: ', ev_menu_configuracion)
            print('VALORES - MENU CONFIGURACION: ', vals_menu_configuracion)
            conf.setConfiguracionesSeleccionadas(ev_menu_configuracion)
            print(conf.getConfiguracionesSeleccionadas())
            if ev_menu_configuracion == 'Configurar' and not ventana_menu_letras_active:
                ventana_menu_letras_active = True
                ventana_menu_configuracion.Hide()
#================================================== CREO EL LAYOUT PARA LA VENTANA DE CONFIGURACION DE LETRAS ==========================================================================
                #COLUMNAS DE LETRAS
                colLet1 = [
                            [sg.Text('', background_color='#00796B')],
                            [sg.Text('A', background_color='#00796B')],
                            [sg.Text('B', background_color='#00796B')],
                            [sg.Text('C', background_color='#00796B')],
                            [sg.Text('D', background_color='#00796B')],
                            [sg.Text('E', background_color='#00796B')],
                            [sg.Text('F', background_color='#00796B')],
                            [sg.Text('G', background_color='#00796B')],
                            [sg.Text('H', background_color='#00796B')],
                            [sg.Text('I', background_color='#00796B')],
                            [sg.Text('J', background_color='#00796B')],
                            [sg.Text('K', background_color='#00796B')],
                            [sg.Text('L', background_color='#00796B')],
                            [sg.Text('M', background_color='#00796B')]
                        ]

                colLet2 = [
                            [sg.Text('', background_color='#00796B')],
                            [sg.Text('N', background_color='#00796B')],
                            [sg.Text('O', background_color='#00796B')],
                            [sg.Text('P', background_color='#00796B')],
                            [sg.Text('Q', background_color='#00796B')],
                            [sg.Text('R', background_color='#00796B')],
                            [sg.Text('S', background_color='#00796B')],
                            [sg.Text('T', background_color='#00796B')],
                            [sg.Text('U', background_color='#00796B')],
                            [sg.Text('V', background_color='#00796B')],
                            [sg.Text('W', background_color='#00796B')],
                            [sg.Text('X', background_color='#00796B')],
                            [sg.Text('Y', background_color='#00796B')],
                            [sg.Text('Z', background_color='#00796B')]
                        ]

                #COLUMNAS DEL INPUT DE CANTIDAD DE LETRAS
                colCant1 = [
                            [sg.Text('Cantidad', background_color='#00796B')],
                            [sg.In(size=(8,5),key='cantA')],
                            [sg.In(size=(8,5),key='cantB')],
                            [sg.In(size=(8,5),key='cantC')],
                            [sg.In(size=(8,5),key='cantD')],
                            [sg.In(size=(8,5),key='cantE')],
                            [sg.In(size=(8,5),key='cantF')],
                            [sg.In(size=(8,5),key='cantG')],
                            [sg.In(size=(8,5),key='cantH')],
                            [sg.In(size=(8,5),key='cantI')],
                            [sg.In(size=(8,5),key='cantJ')],
                            [sg.In(size=(8,5),key='cantK')],
                            [sg.In(size=(8,5),key='cantL')],
                            [sg.In(size=(8,5),key='cantM')]
                ]

                colCant2 = [
                            [sg.Text('Cantidad', background_color='#00796B')],
                            [sg.In(size=(8,5),key='cantN')],
                            [sg.In(size=(8,5),key='cantO')],
                            [sg.In(size=(8,5),key='cantP')],
                            [sg.In(size=(8,5),key='cantQ')],
                            [sg.In(size=(8,5),key='cantR')],
                            [sg.In(size=(8,5),key='cantS')],
                            [sg.In(size=(8,5),key='cantT')],
                            [sg.In(size=(8,5),key='cantU')],
                            [sg.In(size=(8,5),key='cantV')],
                            [sg.In(size=(8,5),key='cantW')],
                            [sg.In(size=(8,5),key='cantX')],
                            [sg.In(size=(8,5),key='cantY')],
                            [sg.In(size=(8,5),key='cantZ')]

                ]

                #COLUMNAS DEL INPUT DEL VALOR DE LAS LETRAS
                colVal1 = [
                            [sg.Text('Valor', background_color='#00796B')],
                            [sg.In(size=(8,5),key='valA')],
                            [sg.In(size=(8,5),key='valB')],
                            [sg.In(size=(8,5),key='valC')],
                            [sg.In(size=(8,5),key='valD')],
                            [sg.In(size=(8,5),key='valE')],
                            [sg.In(size=(8,5),key='valF')],
                            [sg.In(size=(8,5),key='valG')],
                            [sg.In(size=(8,5),key='valH')],
                            [sg.In(size=(8,5),key='valI')],
                            [sg.In(size=(8,5),key='valJ')],
                            [sg.In(size=(8,5),key='valK')],
                            [sg.In(size=(8,5),key='valL')],
                            [sg.In(size=(8,5),key='valM')]
                ]

                colVal2 = [
                            [sg.Text('Valor', background_color='#00796B')],
                            [sg.In(size=(8,5),key='valN')],
                            [sg.In(size=(8,5),key='valO')],
                            [sg.In(size=(8,5),key='valP')],
                            [sg.In(size=(8,5),key='valQ')],
                            [sg.In(size=(8,5),key='valR')],
                            [sg.In(size=(8,5),key='valS')],
                            [sg.In(size=(8,5),key='valT')],
                            [sg.In(size=(8,5),key='valU')],
                            [sg.In(size=(8,5),key='valV')],
                            [sg.In(size=(8,5),key='valW')],
                            [sg.In(size=(8,5),key='valX')],
                            [sg.In(size=(8,5),key='valY')],
                            [sg.In(size=(8,5),key='valZ')]
                ]

                #LAYOUT DONDE JUNTO TODAS LAS COLUMNAS DIVIDIENDOLA EN DOS GRUPOS
                layout_menu_letras = [
                            [sg.Column(colLet1), sg.Column(colCant1),sg.Column(colVal1),sg.Column(colLet2), sg.Column(colCant2),sg.Column(colVal2)],
                            [sg.Button('Aplicar'), sg.Button('Salir')]
                        ]

                # sg.Window('Configuracion de letras', menu_letras)
                ventana_menu_letras = sg.Window('Configuracion de letras', layout_menu_letras)
                while True:
                    ev_menu_letras, vals_menu_letras = ventana_menu_letras.read()

                    if ev_menu_letras == sg.WIN_CLOSED  or ev_menu_letras == 'Salir':
                        ventana_menu_letras.close()
                        ventana_menu_letras_active = False
                        ventana_menu_configuracion.UnHide()
                        break

            if ev_menu_configuracion == sg.WIN_CLOSED or ev_menu_configuracion == 'SIGUIENTE':
                ventana_menu_configuracion.close()
                ventana_menu_configuracion_active = False
                ventana_inicial.UnHide()
                break