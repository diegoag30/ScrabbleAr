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
            'tiempo':'medio',
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

    def configurar_letras(self, diccionario):
        #modifico la cantidad de letras en base a lo ingresado en el input del menu de configurar letras
        if diccionario['cantA'] != '0' and diccionario['cantA'] != '':
            self._configuracion_letras['A']['cant']=int(diccionario['cantA'])
        else:
            print('no pueder ser 0 o campo vacio')
        
        if diccionario['cantB'] != '0' and diccionario['cantB'] != '':
            self._configuracion_letras['B']['cant']=int(diccionario['cantB'])

        if diccionario['cantB'] != '0' and diccionario['cantC'] != '':
            self._configuracion_letras['C']['cant']=int(diccionario['cantC'])

        if diccionario['cantA'] != '0' and diccionario['cantD'] != '':
            self._configuracion_letras['D']['cant']=int(diccionario['cantD'])

        if diccionario['cantA'] != '0' and diccionario['cantE'] != '':
            self._configuracion_letras['E']['cant']=int(diccionario['cantE'])

        if diccionario['cantA'] != '0' and diccionario['cantF'] != '':
            self._configuracion_letras['F']['cant']=int(diccionario['cantF'])

        if diccionario['cantA'] != '0' and diccionario['cantG'] != '':
            self._configuracion_letras['G']['cant']=int(diccionario['cantG'])

        if diccionario['cantA'] != '0' and diccionario['cantH'] != '':
            self._configuracion_letras['H']['cant']=int(diccionario['cantH'])

        if diccionario['cantA'] != '0' and diccionario['cantI'] != '':
            self._configuracion_letras['I']['cant']=int(diccionario['cantI'])

        if diccionario['cantA'] != '0' and diccionario['cantJ'] != '':
            self._configuracion_letras['J']['cant']=int(diccionario['cantJ'])

        if diccionario['cantA'] != '0' and diccionario['cantK'] != '':
            self._configuracion_letras['K']['cant']=int(diccionario['cantK'])

        if diccionario['cantA'] != '0' and diccionario['cantL'] != '':
            self._configuracion_letras['L']['cant']=int(diccionario['cantL'])

        if diccionario['cantA'] != '0' and diccionario['cantM'] != '':
            self._configuracion_letras['M']['cant']=int(diccionario['cantM'])

        if diccionario['cantA'] != '0' and diccionario['cantN'] != '':
            self._configuracion_letras['N']['cant']=int(diccionario['cantN'])

        if diccionario['cantA'] != '0' and diccionario['cantO'] != '':
            self._configuracion_letras['O']['cant']=int(diccionario['cantO'])

        if diccionario['cantA'] != '0' and diccionario['cantP'] != '':
            self._configuracion_letras['P']['cant']=int(diccionario['cantP'])

        if diccionario['cantA'] != '0' and diccionario['cantQ'] != '':
            self._configuracion_letras['Q']['cant']=int(diccionario['cantQ'])

        if diccionario['cantA'] != '0' and diccionario['cantR'] != '':
            self._configuracion_letras['R']['cant']=int(diccionario['cantR'])
            
        if diccionario['cantA'] != '0' and diccionario['cantS'] != '':
            self._configuracion_letras['S']['cant']=int(diccionario['cantS'])

        if diccionario['cantA'] != '0' and diccionario['cantT'] != '':
            self._configuracion_letras['T']['cant']=int(diccionario['cantT'])

        if diccionario['cantA'] != '0' and diccionario['cantU'] != '':
            self._configuracion_letras['U']['cant']=int(diccionario['cantU'])

        if diccionario['cantA'] != '0' and diccionario['cantV'] != '':
            self._configuracion_letras['V']['cant']=int(diccionario['cantV'])

        if diccionario['cantA'] != '0' and diccionario['cantW'] != '':
            self._configuracion_letras['W']['cant']=int(diccionario['cantW'])

        if diccionario['cantA'] != '0' and diccionario['cantX'] != '':
            self._configuracion_letras['X']['cant']=int(diccionario['cantX'])

        if diccionario['cantA'] != '0' and diccionario['cantY'] != '':
            self._configuracion_letras['Y']['cant']=int(diccionario['cantY'])

        if diccionario['cantA'] != '0' and diccionario['cantZ'] != '':
            self._configuracion_letras['Z']['cant']=int(diccionario['cantZ'])

        # self._configuracion_letras['C']['cant']=diccionario['cantC']
        # self._configuracion_letras['D']['cant']=diccionario['cantD']
        # self._configuracion_letras['E']['cant']=diccionario['cantE']
        # self._configuracion_letras['F']['cant']=diccionario['cantF']
        # self._configuracion_letras['G']['cant']=diccionario['cantG']
        # self._configuracion_letras['H']['cant']=diccionario['cantH']
        # self._configuracion_letras['I']['cant']=diccionario['cantI']
        # self._configuracion_letras['J']['cant']=diccionario['cantJ']
        # self._configuracion_letras['K']['cant']=diccionario['cantK']
        # self._configuracion_letras['L']['cant']=diccionario['cantL']
        # self._configuracion_letras['M']['cant']=diccionario['cantM']
        # self._configuracion_letras['N']['cant']=diccionario['cantN']
        # self._configuracion_letras['O']['cant']=diccionario['cantO']
        # self._configuracion_letras['P']['cant']=diccionario['cantP']
        # self._configuracion_letras['Q']['cant']=diccionario['cantQ']
        # self._configuracion_letras['R']['cant']=diccionario['cantR']
        # self._configuracion_letras['S']['cant']=diccionario['cantS']
        # self._configuracion_letras['T']['cant']=diccionario['cantT']
        # self._configuracion_letras['U']['cant']=diccionario['cantU']
        # self._configuracion_letras['V']['cant']=diccionario['cantV']
        # self._configuracion_letras['W']['cant']=diccionario['cantW']
        # self._configuracion_letras['X']['cant']=diccionario['cantX']
        # self._configuracion_letras['Y']['cant']=diccionario['cantY']
        # self._configuracion_letras['Z']['cant']=diccionario['cantZ']
         
        if diccionario['valA'] != '0' and diccionario['cantA'] != '':
            self._configuracion_letras['A']['val']=int(diccionario['valA'])
        if diccionario['valB'] != '0' and diccionario['cantB'] != '':
            self._configuracion_letras['B']['val']=int(diccionario['valB'])
        if diccionario['valC'] != '0' and diccionario['cantC'] != '':
            self._configuracion_letras['C']['val']=int(diccionario['valC'])
        if diccionario['valD'] != '0' and diccionario['cantD'] != '':
            self._configuracion_letras['D']['val']=int(diccionario['valD'])
        if diccionario['valE'] != '0' and diccionario['cantE'] != '':
            self._configuracion_letras['E']['val']=int(diccionario['valE'])
        if diccionario['valF'] != '0' and diccionario['cantF'] != '':
            self._configuracion_letras['F']['val']=int(diccionario['valF'])
        if diccionario['valG'] != '0' and diccionario['cantG'] != '':
            self._configuracion_letras['G']['val']=int(diccionario['valG'])
        if diccionario['valH'] != '0' and diccionario['cantH'] != '':
            self._configuracion_letras['H']['val']=int(diccionario['valH'])
        if diccionario['valI'] != '0' and diccionario['cantI'] != '':
            self._configuracion_letras['I']['val']=int(diccionario['valI'])
        if diccionario['valJ'] != '0' and diccionario['cantJ'] != '':
            self._configuracion_letras['J']['val']=int(diccionario['valJ'])
        if diccionario['valK'] != '0' and diccionario['cantK'] != '':
            self._configuracion_letras['K']['val']=int(diccionario['valK'])
        if diccionario['valL'] != '0' and diccionario['cantL'] != '':
            self._configuracion_letras['L']['val']=int(diccionario['valL'])
        if diccionario['valM'] != '0' and diccionario['cantM'] != '':
            self._configuracion_letras['M']['val']=int(diccionario['valM'])
        if diccionario['valN'] != '0' and diccionario['cantN'] != '':
            self._configuracion_letras['N']['val']=int(diccionario['valN'])
        if diccionario['valO'] != '0' and diccionario['cantO'] != '':
            self._configuracion_letras['O']['val']=int(diccionario['valO'])
        if diccionario['valP'] != '0' and diccionario['cantP'] != '':
            self._configuracion_letras['P']['val']=int(diccionario['valP'])
        if diccionario['valQ'] != '0' and diccionario['cantQ'] != '':
            self._configuracion_letras['Q']['val']=int(diccionario['valQ'])
        if diccionario['valR'] != '0' and diccionario['cantR'] != '':
            self._configuracion_letras['R']['val']=int(diccionario['valR'])
        if diccionario['valS'] != '0' and diccionario['cantS'] != '':
            self._configuracion_letras['S']['val']=int(diccionario['valS'])
        if diccionario['valT'] != '0' and diccionario['cantT'] != '':
            self._configuracion_letras['T']['val']=int(diccionario['valT'])
        if diccionario['valU'] != '0' and diccionario['cantU'] != '':
            self._configuracion_letras['U']['val']=int(diccionario['valU'])
        if diccionario['valV'] != '0' and diccionario['cantV'] != '':
            self._configuracion_letras['V']['val']=int(diccionario['valV'])
        if diccionario['valW'] != '0' and diccionario['cantW'] != '':
            self._configuracion_letras['W']['val']=int(diccionario['valW'])
        if diccionario['valX'] != '0' and diccionario['cantX'] != '':
            self._configuracion_letras['X']['val']=int(diccionario['valX'])
        if diccionario['valY'] != '0' and diccionario['cantY'] != '':
            self._configuracion_letras['Y']['val']=int(diccionario['valY'])
        if diccionario['valZ'] != '0' and diccionario['cantZ'] != '':
            self._configuracion_letras['Z']['val']=int(diccionario['valZ'])



        #modifico el valor del puntaje de las letras en base a lo ingresado en el input del menu de configurar letras
        # self._configuracion_letras['A']['val']=diccionario['valA']
        # self._configuracion_letras['B']['val']=diccionario['valB']
        # self._configuracion_letras['C']['val']=diccionario['valC']
        # self._configuracion_letras['D']['val']=diccionario['valD']
        # self._configuracion_letras['E']['val']=diccionario['valE']
        # self._configuracion_letras['F']['val']=diccionario['valF']
        # self._configuracion_letras['G']['val']=diccionario['valG']
        # self._configuracion_letras['H']['val']=diccionario['valH']
        # self._configuracion_letras['I']['val']=diccionario['valI']
        # self._configuracion_letras['J']['val']=diccionario['valJ']
        # self._configuracion_letras['K']['val']=diccionario['valK']
        # self._configuracion_letras['L']['val']=diccionario['valL']
        # self._configuracion_letras['M']['val']=diccionario['valM']
        # self._configuracion_letras['N']['val']=diccionario['valN']
        # self._configuracion_letras['O']['val']=diccionario['valO']
        # self._configuracion_letras['P']['val']=diccionario['valP']
        # self._configuracion_letras['Q']['val']=diccionario['valQ']
        # self._configuracion_letras['R']['val']=diccionario['valR']
        # self._configuracion_letras['S']['val']=diccionario['valS']
        # self._configuracion_letras['T']['val']=diccionario['valT']
        # self._configuracion_letras['U']['val']=diccionario['valU']
        # self._configuracion_letras['V']['val']=diccionario['valV']
        # self._configuracion_letras['W']['val']=diccionario['valW']
        # self._configuracion_letras['X']['val']=diccionario['valX']
        # self._configuracion_letras['Y']['val']=diccionario['valY']
        # self._configuracion_letras['Z']['val']=diccionario['valZ']