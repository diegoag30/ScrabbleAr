import PySimpleGUI as sg

"""
    IMPORTANTE: ESTO LO VOY A BORRAR A FUTURO CUANDO NO LO NECESITE MAS, DE MOMENTO LO USO DE PRUEBA Y RESPALDO
"""

color_de_fondo = '#00796B'

sg.theme_background_color(color='#00796B')


menu_def = [['File', ['Open', 'Save', 'Exit',]],
               ['Edit', ['Paste', ['Special', 'Normal',], 'Undo'],],
               ['Help', 'About...'],]

layout = [
            [sg.Menu(menu_def)],
            [sg.Image(r'app/images/scrabble_logo508x214.png', size=(1000, 300), pad=((0,0),(200,0)), background_color='#00796B')],
            [sg.Button(button_color=(sg.theme_background_color(), sg.theme_background_color()), image_filename='app/images/play.png', image_size=(256, 256), key='LOGO', image_subsample=2, border_width=0,pad=((110,0),(0,100))), 
            sg.Button(button_color=(sg.theme_background_color(), sg.theme_background_color()), image_filename='app/images/star.png', image_size=(256, 256), key='RANKING', image_subsample=2, border_width=0,pad=((0,0),(0,100))), 
            sg.Button(button_color=(sg.theme_background_color(), sg.theme_background_color()), image_filename='app/images/configuracion.png', image_size=(256, 256), key='CONFIGURACION', image_subsample=2, border_width=0,pad=((0,0),(0,100)))]
         ]

# sg.Button(image_filename='play2.png', image_size=(128,128), button_color=(None,'#00796B'), pad=((600,0),(0,50)))

menu = [
    [sg.Text('Tiempo de juego', background_color=color_de_fondo, text_color='white', font=('Helvetica', 15, 'bold'))],
    [sg.Radio('Rapido', "RADIO1", default=True, background_color=color_de_fondo, text_color='white', font=('Helvetica', 12, 'bold'), key='rapido'),sg.Radio('Medio', "RADIO1", background_color=color_de_fondo, text_color='white', font=('Helvetica', 12, 'bold'), key='normal'),sg.Radio('Lento', "RADIO1", background_color=color_de_fondo, text_color='white', font=('Helvetica', 12, 'bold'), key='lento')],
    [sg.Text('Nivel de dificultad', background_color=color_de_fondo, text_color='white', font=('Helvetica', 15, 'bold'))],
    [sg.Radio('Facil', "RADIO2", default=True, background_color=color_de_fondo, text_color='white', font=('Helvetica', 12, 'bold'),key='facil'),sg.Radio('Medio', "RADIO2", background_color=color_de_fondo, text_color='white', font=('Helvetica', 12, 'bold'), key='medio'),sg.Radio('Dificil', "RADIO2", background_color=color_de_fondo, text_color='white', font=('Helvetica', 12, 'bold'), key='dificil')],
    [sg.Text('Puntaje de cada letra', background_color=color_de_fondo, text_color='white', font=('Helvetica', 15, 'bold'))],
    [sg.Text('    ○ 1 Punto   ', background_color=color_de_fondo, font=('Helvetica', 12, 'bold')), sg.In(key='1p')],
    [sg.Text('    ○ 2 Puntos  ', background_color=color_de_fondo, font=('Helvetica', 12, 'bold')), sg.In(key='2p')],
    [sg.Text('    ○ 3 Puntos  ', background_color=color_de_fondo, font=('Helvetica', 12, 'bold')), sg.In(key='3p')],
    [sg.Text('    ○ 4 Puntos  ', background_color=color_de_fondo, font=('Helvetica', 12, 'bold')), sg.In(key='4p')],
    [sg.Text('    ○ 6 Puntos  ', background_color=color_de_fondo, font=('Helvetica', 12, 'bold')), sg.In(key='6p')],
    [sg.Text('    ○ 8 Puntos  ', background_color=color_de_fondo, font=('Helvetica', 12, 'bold')), sg.In(key='8p')],
    [sg.Text('    ○ 10 Puntos ', background_color=color_de_fondo, font=('Helvetica', 12, 'bold')), sg.In(key='10p')],
    [sg.Button('SIGUIENTE')]
]



configuracion = [
    # [sg.Text('Tiempo de juego', background_color=color_de_fondo, text_color='white', font=('Helvetica', 15, 'bold'), pad=((446,0),(15,15)), tooltip=('Elije el tiempo que durara la partida'))],
    [sg.Image(r'app/images/tiempo_de_juego.png', tooltip=('Elige el tiempo que durara la partida'), size=(650, 50), pad=((200,0),(10,10)), background_color='#00796B')],
    [sg.Button(button_color=(sg.theme_background_color(), sg.theme_background_color()), image_filename='app/images/minimo_375x138.png', image_size=(170, 64), key='minimo', image_subsample=2, border_width=0,pad=((440,0),(0,0)), tooltip=('Elija esta opción si quiere jugar una partida rapida'))],
    [sg.Button(button_color=(sg.theme_background_color(), sg.theme_background_color()), image_filename='app/images/medio_375x138.png', image_size=(170, 64), key='medio', image_subsample=2, border_width=0,pad=((440,0),(0,0)), tooltip=('Elija esta opción si quiere jugar una partida normal'))],
    [sg.Button(button_color=(sg.theme_background_color(), sg.theme_background_color()), image_filename='app/images/maximo_375x138.png', image_size=(170, 64), key='maximo', image_subsample=2, border_width=0,pad=((440,0),(0,0)), tooltip=('Elija esta opción si quiere jugar una partida con mucho tiempo'))],
    # [sg.Text('Nivel de dificultad', background_color=color_de_fondo, text_color='white', font=('Helvetica', 15, 'bold'), pad=((441,0),(15,15)), tooltip=('En esta opción, se configurará el nivel del juego.'))],
    [sg.Image(r'app/images/nivel_de_dificultad.png', tooltip=('En esta opción, se configurará el nivel del juego.'), size=(650, 50), pad=((200,0),(10,10)), background_color='#00796B')],
    [sg.Button(button_color=(sg.theme_background_color(), sg.theme_background_color()), image_filename='app/images/facil_375x138.png', image_size=(170, 64), key='facil', image_subsample=2, border_width=0,pad=((440,0),(0,0)), tooltip=('Se jugara con cualquier tipo de palabra (adjetivos, sustantivos y verbos).'))],
    [sg.Button(button_color=(sg.theme_background_color(), sg.theme_background_color()), image_filename='app/images/normal_375x138.png', image_size=(170, 64), key='normal', image_subsample=2, border_width=0,pad=((440,0),(0,0)), tooltip=('Se jugara sólo con verbos y adjetivos.'))],
    [sg.Button(button_color=(sg.theme_background_color(), sg.theme_background_color()), image_filename='app/images/dificil_375x138.png', image_size=(170, 64), key='dificil', image_subsample=2, border_width=0,pad=((440,0),(0,0)), tooltip=('Se jugara con una categoría elegida al azar entre verbos y adjetivos.'))],
    # [sg.Text('Seleccionar Tablero', tooltip=('Elija entre uno de los tres tableros disponibles para jugar, por defecto se elije el tablero 1'), background_color=color_de_fondo, text_color='white', font=('Helvetica', 15, 'bold'), pad=((430,0),(15,15)))],
    [sg.Image(r'app/images/modelo_de_tablero.png', tooltip=('Elija entre uno de los tres tableros disponibles para jugar, por defecto se elije el tablero 1'), size=(650, 50), pad=((200,0),(10,10)), background_color='#00796B')],
    #para el diseño de los tableros uso imagenes por defecto hasta que se pueda visualizar los 3 tableros para realizar una miniatura
    [sg.Button(button_color=(sg.theme_background_color(), sg.theme_background_color()), image_filename='app/images/tablero_1.png', image_size=(171,171), key='tablero_1', image_subsample=3, border_width=0,pad=((218,0),(0,0)), tooltip=('Tablero dieñado por Cristian')),
    sg.Button(button_color=(sg.theme_background_color(), sg.theme_background_color()), image_filename='app/images/tablero_2.png', image_size=(171,171), key='tablero_2', image_subsample=3, border_width=0,pad=((50,0),(0,0)), tooltip=('Tablero de ejemplo')),
    sg.Button(button_color=(sg.theme_background_color(), sg.theme_background_color()), image_filename='app/images/tablero_3.png', image_size=(171,171), key='tablero_3', image_subsample=3, border_width=0,pad=((50,0),(0,0)), tooltip=('Tablero de ejemplo'))],
    [sg.Button('SIGUIENTE')]
]

window = sg.Window("Scrabble GO", layout, icon='ScrabbleGO.ico')

configuraciones_seleccionadas = {
    'tiempo':'medio',
    'dificultad':'normal',
    'tablero':1
}

while True:
    event, values = window.read()
    print(event, values)
    print("eventos: ",event,"valores: ", values)
    if event == sg.WIN_CLOSED:
        break
    if event == 'CONFIGURACION':
        window.close(); del window
        window = sg.Window('Scrabble GO - Configuracion', configuracion, icon='ScrabbleGO.ico', size=(1050,850))
        # event, values = window.read()
        # if event == 'facil':
        #     configuraciones_seleccionadas['dificultad'] = 'facil'
        # elif event == 'normal':
        #     configuraciones_seleccionadas['dificultad'] = 'normal'
        # elif event == 'dificil':
        #     configuraciones_seleccionadas['dificultad'] = 'dificil'
        # elif event == 'minimo':
        #     configuraciones_seleccionadas['tiempo'] = 'minimo'
        # elif event == 'medio':
        #     configuraciones_seleccionadas['tiempo'] = 'medio'
        # else:
        #     configuraciones_seleccionadas['tiempo'] = 'maximo'
        if event == 'SIGUIENTE':
            print('hola')
            event, values = window.read()
            print(event, values)
        