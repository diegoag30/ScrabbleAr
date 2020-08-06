import PySimpleGUI as sg
import random

class Configuracion():
    """
        Esta clase se encarga de establecer y cambiar todos los parametros del juego.
        Si no se configura ningun parametro en la seccion menu que se da en la pantalla inicial, se tomara los valores por defectos, cuyos valores son:
            - Tiempo de juego: Normal
            - Nivel: Medio (sólo se podrán agregar adjetivos o verbos)
            - Puntaje de cada ficha:
                - 1 punto: A, E, O, S, I, U, N, L, R, T
                - 2 puntos: C, D, G
                - 3 puntos: M, B, P
                - 4 puntos: F, H, V, Y
                - 6 puntos: J
                - 8 puntos: K, LL, Ñ, Q, RR, W, X
                - 10 puntos: Z
            - Cantidad total de fichas por letra:
                - A ×11, E ×11, O ×8, S ×7, I ×6, U ×6, N ×5, L ×4, R ×4, T ×4
                - C ×4, D ×4, G ×2
                - M ×3, B ×3, P ×2
                - F ×2, H ×2, V ×2, Y ×1
                - J ×2
                - K ×1, LL ×1, Ñ ×1, Q ×1, RR ×1, W ×1, X ×1
                - Z ×1
            - TERMINARE DE COMPLETAR ESTO CUANDO DECIDA BIEN CUALES SERAN LOS VALORES POR DEFECTO.
    """



    # color_de_fondo = '#00796B'

    # sg.theme_background_color(color='#00796B')

    # menu_def = [['File', ['Open', 'Save', 'Exit',]],
    #            ['Edit', ['Paste', ['Special', 'Normal',], 'Undo'],],
    #            ['Help', 'About...'],]
    # layout = [
    #             [sg.Menu(menu_def)],
    #             [sg.Image(r'menu/images/logo_scrabble.png', size=(1280, 300), pad=((0,0),(200,0)), background_color='#00796B')],
    #             [sg.Button(button_color=(sg.theme_background_color(), sg.theme_background_color()), image_filename='menu/images/play.png', image_size=(256, 256), key='LOGO', image_subsample=2, border_width=0,pad=((270,0),(0,100))),
    #             sg.Button(button_color=(sg.theme_background_color(), sg.theme_background_color()), image_filename='menu/images/star.png', image_size=(256, 256), key='RANKING', image_subsample=2, border_width=0,pad=((0,0),(0,100))),
    #             sg.Button(button_color=(sg.theme_background_color(), sg.theme_background_color()), image_filename='menu/images/configuracion.png', image_size=(256, 256), key='CONFIGURACION', image_subsample=2, border_width=0,pad=((0,0),(0,100)))]
    #         ]
    # menu = [
    #     [sg.Text('Tiempo de juego', background_color=color_de_fondo, text_color='white', font=('Helvetica', 15, 'bold'))],
    #     [sg.Radio('Rapido', "RADIO1", default=True, background_color=color_de_fondo, text_color='white', font=('Helvetica', 12, 'bold'), key='rapido'),sg.Radio('Medio', "RADIO1", background_color=color_de_fondo, text_color='white', font=('Helvetica', 12, 'bold'), key='normal'),sg.Radio('Lento', "RADIO1", background_color=color_de_fondo, text_color='white', font=('Helvetica', 12, 'bold'), key='lento')],
    #     [sg.Text('Nivel de dificultad', background_color=color_de_fondo, text_color='white', font=('Helvetica', 15, 'bold'))],
    #     [sg.Radio('Facil', "RADIO2", default=True, background_color=color_de_fondo, text_color='white', font=('Helvetica', 12, 'bold'),key='facil'),sg.Radio('Medio', "RADIO2", background_color=color_de_fondo, text_color='white', font=('Helvetica', 12, 'bold'), key='medio'),sg.Radio('Dificil', "RADIO2", background_color=color_de_fondo, text_color='white', font=('Helvetica', 12, 'bold'), key='dificil')],
    #     [sg.Text('Puntaje de cada letra', background_color=color_de_fondo, text_color='white', font=('Helvetica', 15, 'bold'))],
    #     [sg.Text('    ○ 1 Punto   ', background_color=color_de_fondo, font=('Helvetica', 12, 'bold')), sg.In(key='1p')],
    #     [sg.Text('    ○ 2 Puntos  ', background_color=color_de_fondo, font=('Helvetica', 12, 'bold')), sg.In(key='2p')],
    #     [sg.Text('    ○ 3 Puntos  ', background_color=color_de_fondo, font=('Helvetica', 12, 'bold')), sg.In(key='3p')],
    #     [sg.Text('    ○ 4 Puntos  ', background_color=color_de_fondo, font=('Helvetica', 12, 'bold')), sg.In(key='4p')],
    #     [sg.Text('    ○ 6 Puntos  ', background_color=color_de_fondo, font=('Helvetica', 12, 'bold')), sg.In(key='6p')],
    #     [sg.Text('    ○ 8 Puntos  ', background_color=color_de_fondo, font=('Helvetica', 12, 'bold')), sg.In(key='8p')],
    #     [sg.Text('    ○ 10 Puntos ', background_color=color_de_fondo, font=('Helvetica', 12, 'bold')), sg.In(key='10p')],
    #     [sg.Button('SIGUIENTE')]
    # ]

    def __init__(self):
        self._color_de_fondo = '#00796B'

        # sg.theme_background_color(color='#00796B')

        self._menu_def = [['File', ['Open', 'Save', 'Exit',]],
               ['Edit', ['Paste', ['Special', 'Normal',], 'Undo'],],
               ['Help', 'About...'],
               ]
        self._layout = [
            [sg.Menu(self._menu_def)],
            [sg.Image(r'app/images/scrabble_logo508x214.png', size=(1000, 300), pad=((0,0),(200,0)), background_color='#00796B')],
            [sg.Button(button_color=(sg.theme_background_color(), sg.theme_background_color()), image_filename='app/images/play.png', image_size=(256, 256), key='LOGO', image_subsample=2, border_width=0,pad=((110,0),(0,100))), 
            sg.Button(button_color=(sg.theme_background_color(), sg.theme_background_color()), image_filename='app/images/star.png', image_size=(256, 256), key='RANKING', image_subsample=2, border_width=0,pad=((0,0),(0,100))), 
            sg.Button(button_color=(sg.theme_background_color(), sg.theme_background_color()), image_filename='app/images/configuracion.png', image_size=(256, 256), key='CONFIGURACION', image_subsample=2, border_width=0,pad=((0,0),(0,100)))]
         ]

        self._configuracion = [
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
            [sg.Button('Configurar letras')],
            [sg.Button('SIGUIENTE')]
            ]

        self._configuraciones_seleccionadas = {
            'tiempo':'dificil',
            'dificultad':'normal',
            'tablero':1
            }      
        
        self._lista_random_clasificacion = ['JJ', 'VB']
        self._clasificacion_seleccionada = random.choice(self._lista_random_clasificacion)
        # self._clasificacion_seleccionada = ''

        self._configuracion_letras = {
            'A':{'cant':11,'val':1},
            'B':{'cant':3,'val':3},
            'C':{'cant':4,'val':2},
            'D':{'cant':4,'val':2},
            'E':{'cant':11,'val':1},
            'F':{'cant':2,'val':4},
            'G':{'cant':2,'val':2},
            'H':{'cant':2,'val':4},
            'I':{'cant':6,'val':1},
            'J':{'cant':2,'val':6},
            'K':{'cant':1,'val':8},
            'L':{'cant':4,'val':1},
            'M':{'cant':3,'val':3},
            'N':{'cant':5,'val':1},
            'O':{'cant':8,'val':1},
            'P':{'cant':2,'val':3},
            'Q':{'cant':1,'val':8},
            'R':{'cant':4,'val':1},
            'S':{'cant':7,'val':1},
            'T':{'cant':4,'val':1},
            'U':{'cant':6,'val':1},
            'V':{'cant':2,'val':4},
            'W':{'cant':1,'val':8},
            'X':{'cant':1,'val':8},
            'Y':{'cant':1,'val':4},
            'Z':{'cant':1,'val':10}
        }

    def get_tablero_elegido(self):
        return self._configuraciones_seleccionadas["tablero"]

    def getLayout(self):
        return self._layout

    def getMenu(self):
        return self._configuracion

    def ventanaPrincipal(self):
        return (sg.Window("Scrabble GO", self._layout, icon='ScrabbleGO.ico'))
    
    def menuConfiguracion(self):
        return (sg.Window("Scrabble GO", self._configuracion, icon='ScrabbleGO.ico', size=(1050,850)))

    def opciones_elegidas(self, eventos):
        pass

    def setConfiguracionesSeleccionadas(self, evento):
        if evento == 'facil':
            self._configuraciones_seleccionadas['dificultad'] = 'facil'
        if evento == 'normal':
            self._configuraciones_seleccionadas['dificultad'] = 'normal'
        if evento == 'dificil':
            self._configuraciones_seleccionadas['dificultad'] = 'dificil'
            #hago una seleccion random del tipo de palabra a usar en caso que se selecciono la dificultad en dificil
            self._clasificacion_seleccionada = random.choice(self._lista_random_clasificacion)
        if evento == 'minimo':
            self._configuraciones_seleccionadas['tiempo'] = 'minimo'
        if evento == 'medio':
            self._configuraciones_seleccionadas['tiempo'] = 'medio'
        if evento == 'maximo':
            self._configuraciones_seleccionadas['tiempo'] = 'maximo'
        if evento == 'tablero_1':
            self._configuraciones_seleccionadas['tablero'] = 1
        if evento == 'tablero_2':
            self._configuraciones_seleccionadas['tablero'] = 2
        if evento == 'tablero_3':
            self._configuraciones_seleccionadas['tablero'] = 3

    def getClasificacionSeleccionada(self):
        return self._clasificacion_seleccionada

    def getConfiguracionesSeleccionadas(self):
        """Metodo que devuelve las opciones que se eligieron en el menu de configuracion"""
        return self._configuraciones_seleccionadas

    def getConfiguracionLetras(self):
        return self._configuracion_letras

    def setConfiguracionLetras(self, diccionario):
        self._configuracion_letras = diccionario

    def layoutVentanaInicial(self):
        return self._layout