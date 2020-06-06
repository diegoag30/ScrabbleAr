import PySimpleGUI as sg

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
                            [sg.Image(r'menu/images/logo_scrabble.png', size=(1280, 300), pad=((0,0),(200,0)), background_color='#00796B')],
                            [sg.Button(button_color=(sg.theme_background_color(), sg.theme_background_color()), image_filename='menu/images/play.png', image_size=(256, 256), key='LOGO', image_subsample=2, border_width=0,pad=((270,0),(0,100))),
                            sg.Button(button_color=(sg.theme_background_color(), sg.theme_background_color()), image_filename='menu/images/star.png', image_size=(256, 256), key='RANKING', image_subsample=2, border_width=0,pad=((0,0),(0,100))),
                            sg.Button(button_color=(sg.theme_background_color(), sg.theme_background_color()), image_filename='menu/images/configuracion.png', image_size=(256, 256), key='CONFIGURACION', image_subsample=2, border_width=0,pad=((0,0),(0,100)))]
                     ]

        self._menu = [
                            [sg.Text('Tiempo de juego', background_color=self._color_de_fondo, text_color='white', font=('Helvetica', 15, 'bold'))],
                            [sg.Radio('Rapido', "RADIO1", default=True, background_color=self._color_de_fondo, text_color='white', font=('Helvetica', 12, 'bold'), key='rapido'),sg.Radio('Medio', "RADIO1", background_color=self._color_de_fondo, text_color='white', font=('Helvetica', 12, 'bold'), key='normal'),sg.Radio('Lento', "RADIO1", background_color=self._color_de_fondo, text_color='white', font=('Helvetica', 12, 'bold'), key='lento')],
                            [sg.Text('Nivel de dificultad', background_color=self._color_de_fondo, text_color='white', font=('Helvetica', 15, 'bold'))],
                            [sg.Radio('Facil', "RADIO2", default=True, background_color=self._color_de_fondo, text_color='white', font=('Helvetica', 12, 'bold'),key='facil'),sg.Radio('Medio', "RADIO2", background_color=self._color_de_fondo, text_color='white', font=('Helvetica', 12, 'bold'), key='medio'),sg.Radio('Dificil', "RADIO2", background_color=self._color_de_fondo, text_color='white', font=('Helvetica', 12, 'bold'), key='dificil')],
                            [sg.Text('Puntaje de cada letra', background_color=self._color_de_fondo, text_color='white', font=('Helvetica', 15, 'bold'))],
                            [sg.Text('    ○ 1 Punto   ', background_color=self._color_de_fondo, font=('Helvetica', 12, 'bold')), sg.In(key='1p')],
                            [sg.Text('    ○ 2 Puntos  ', background_color=self._color_de_fondo, font=('Helvetica', 12, 'bold')), sg.In(key='2p')],
                            [sg.Text('    ○ 3 Puntos  ', background_color=self._color_de_fondo, font=('Helvetica', 12, 'bold')), sg.In(key='3p')],
                            [sg.Text('    ○ 4 Puntos  ', background_color=self._color_de_fondo, font=('Helvetica', 12, 'bold')), sg.In(key='4p')],
                            [sg.Text('    ○ 6 Puntos  ', background_color=self._color_de_fondo, font=('Helvetica', 12, 'bold')), sg.In(key='6p')],
                            [sg.Text('    ○ 8 Puntos  ', background_color=self._color_de_fondo, font=('Helvetica', 12, 'bold')), sg.In(key='8p')],
                            [sg.Text('    ○ 10 Puntos ', background_color=self._color_de_fondo, font=('Helvetica', 12, 'bold')), sg.In(key='10p')],
                            [sg.Button('SIGUIENTE')]
                    ]


    def getLayout(self):
        return self._layout

    def getMenu(self):
        return self._menu

    def ventanaPrincipal(self):
        return (sg.Window("Scrabble GO", self._layout, icon='ScrabbleGO.ico'))
    
    def menuConfiguracion(self):
        return (sg.Window("Scrabble GO", self._menu, icon='ScrabbleGO.ico', size=(1302,800)))

