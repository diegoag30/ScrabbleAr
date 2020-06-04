import PySimpleGUI as sg

color_de_fondo = '#00796B'

sg.theme_background_color(color='#00796B')


menu_def = [['File', ['Open', 'Save', 'Exit',]],
               ['Edit', ['Paste', ['Special', 'Normal',], 'Undo'],],
               ['Help', 'About...'],]

layout = [
            [sg.Menu(menu_def)],
            [sg.Image(r'menu/images/logo_scrabble.png', size=(1280, 300), pad=((0,0),(200,0)), background_color='#00796B')],
            [sg.Button(button_color=(sg.theme_background_color(), sg.theme_background_color()), image_filename='menu/images/play.png', image_size=(256, 256), key='LOGO', image_subsample=2, border_width=0,pad=((270,0),(0,100))), 
            sg.Button(button_color=(sg.theme_background_color(), sg.theme_background_color()), image_filename='menu/images/star.png', image_size=(256, 256), key='RANKING', image_subsample=2, border_width=0,pad=((0,0),(0,100))), 
            sg.Button(button_color=(sg.theme_background_color(), sg.theme_background_color()), image_filename='menu/images/configuracion.png', image_size=(256, 256), key='CONFIGURACION', image_subsample=2, border_width=0,pad=((0,0),(0,100)))]
         ]

# sg.Button(image_filename='play2.png', image_size=(128,128), button_color=(None,'#00796B'), pad=((600,0),(0,50)))

menu = [
    [sg.Text('Tiempo de juego', background_color=color_de_fondo, text_color='white', font=('Helvetica', 15, 'bold'))],
    [sg.Radio('Rapido', "RADIO1", default=True, background_color=color_de_fondo, text_color='white', font=('Helvetica', 12, 'bold')),sg.Radio('Medio', "RADIO1", background_color=color_de_fondo, text_color='white', font=('Helvetica', 12, 'bold')),sg.Radio('Lento', "RADIO1", background_color=color_de_fondo, text_color='white', font=('Helvetica', 12, 'bold'))],
    [sg.Text('Nivel de dificultad', background_color=color_de_fondo, text_color='white', font=('Helvetica', 15, 'bold'))],
    [sg.Radio('Facil', "RADIO1", default=True, background_color=color_de_fondo, text_color='white', font=('Helvetica', 12, 'bold')),sg.Radio('Medio', "RADIO1", background_color=color_de_fondo, text_color='white', font=('Helvetica', 12, 'bold')),sg.Radio('Dificil', "RADIO1", background_color=color_de_fondo, text_color='white', font=('Helvetica', 12, 'bold'))],
    [sg.Text('Puntaje de cada letra', background_color=color_de_fondo, text_color='white', font=('Helvetica', 15, 'bold'))],
    [sg.Text('    ○ 1 Punto   ', background_color=color_de_fondo, font=('Helvetica', 12, 'bold')), sg.In(key='1p')],
    [sg.Text('    ○ 2 Puntos  ', background_color=color_de_fondo, font=('Helvetica', 12, 'bold')), sg.In(key='2p')],
    [sg.Text('    ○ 3 Puntos  ', background_color=color_de_fondo, font=('Helvetica', 12, 'bold')), sg.In(key='3p')],
    [sg.Text('    ○ 4 Puntos  ', background_color=color_de_fondo, font=('Helvetica', 12, 'bold')), sg.In(key='4p')],
    [sg.Text('    ○ 6 Puntos  ', background_color=color_de_fondo, font=('Helvetica', 12, 'bold')), sg.In(key='6p')],
    [sg.Text('    ○ 8 Puntos  ', background_color=color_de_fondo, font=('Helvetica', 12, 'bold')), sg.In(key='8p')],
    [sg.Text('    ○ 10 Puntos ', background_color=color_de_fondo, font=('Helvetica', 12, 'bold')), sg.In(key='10p')],
    [sg.Button('AVANZADA')]
]

window = sg.Window("Scrabble GO", layout)

while True:
    event, values = window.read()
    print(event, values)
    if event == sg.WIN_CLOSED:
        break
    if event == 'CONFIGURACION':
        window.close(); del window
        window = sg.Window('Scrabble GO - Configuracion', menu)
        event, values = window.read()
        