import PySimpleGUI as sg

"""
    MODULO PARA REALIZAR LA CONFIGURACION DE LA CANTIDAD Y VALOR DE CADA LETRA.
    TANTO LA CANTIDAD DE LETRAS COMO LA CANTIDAD DE VALORES, TENDRAN UNA CONFIGURACION CON VALORES POR DEFECTO.
    ESTE MODULO SERA AGREGADO AL MENU DE CONFIGURACION COMO UNA CONFIGURACION QUE SE ABRIRA CON UNA PANTALLA APARTE DE MOMENTO.
"""

# layout = [
#             [sg.Text('Cantidad'), sg.Text('Valor')],
#             [sg.Text('A'), sg.In(size=(5,5),key=1), sg.In(size=(5,5) ,key=1)],
#             [sg.Text('B'), sg.In(size=(5,5),key=2), sg.In(size=(5,5),key=1)],
#             [sg.Text('C'), sg.In(size=(5,5),key=3), sg.In(size=(5,5),key=1)],
#             [sg.Text('D'), sg.In(size=(5,5),key=4), sg.In(size=(5,5),key=1)],
#             [sg.Text('E'), sg.In(size=(5,5),key=6), sg.In(size=(5,5),key=1)],
#             [sg.Text('F'), sg.In(size=(5,5),key=8), sg.In(size=(5,5),key=1)],
#             [sg.Text('G'), sg.In(size=(5,5),key=10), sg.In(size=(5,5),key=1)],
#             [sg.Button('Save'), sg.Button('Exit')]
#          ]

# col1 = [[sg.Text('Cantidad'), sg.Text('Valor')],
#             [sg.Text('A'), sg.In(size=(5,5),key='A'), sg.In(size=(5,5) ,key=1)],
#             [sg.Text('B'), sg.In(size=(5,5),key='B'), sg.In(size=(5,5),key=2)],
#             [sg.Text('C'), sg.In(size=(5,5),key='C'), sg.In(size=(5,5),key=3)],
#             [sg.Text('D'), sg.In(size=(5,5),key='D'), sg.In(size=(5,5),key=4)],
#             [sg.Text('E'), sg.In(size=(5,5),key='E'), sg.In(size=(5,5),key=5)],
#             [sg.Text('F'), sg.In(size=(5,5),key='F'), sg.In(size=(5,5),key=6)],
#             [sg.Text('G'), sg.In(size=(5,5),key='G'), sg.In(size=(5,5),key=7)],
#             [sg.Text('H'), sg.In(size=(5,5),key='H'), sg.In(size=(5,5),key=8)],
#             [sg.Text('I'), sg.In(size=(5,5),key='I'), sg.In(size=(5,5),key=9)],
#             [sg.Text('J'), sg.In(size=(5,5),key='J'), sg.In(size=(5,5),key=10)],
#             [sg.Text('K'), sg.In(size=(5,5),key='K'), sg.In(size=(5,5),key=11)],
#             [sg.Text('L'), sg.In(size=(5,5),key='L'), sg.In(size=(5,5),key=12)],
#             [sg.Text('M'), sg.In(size=(5,5),key='M'), sg.In(size=(5,5),key=13)]
#             ]

# col2 = [[sg.Text('Cantidad'), sg.Text('Valor')],
#             [sg.Text('N'), sg.In(size=(5,5),key='N'), sg.In(size=(5,5) ,key=14)],
#             [sg.Text('O'), sg.In(size=(5,5),key='O'), sg.In(size=(5,5),key=15)],
#             [sg.Text('P'), sg.In(size=(5,5),key='P'), sg.In(size=(5,5),key=16)],
#             [sg.Text('Q'), sg.In(size=(5,5),key='Q'), sg.In(size=(5,5),key=17)],
#             [sg.Text('R'), sg.In(size=(5,5),key='R'), sg.In(size=(5,5),key=18)],
#             [sg.Text('S'), sg.In(size=(5,5),key='S'), sg.In(size=(5,5),key=19)],
#             [sg.Text('T'), sg.In(size=(5,5),key='T'), sg.In(size=(5,5),key=20)],
#             [sg.Text('U'), sg.In(size=(5,5),key='U'), sg.In(size=(5,5),key=21)],
#             [sg.Text('V'), sg.In(size=(5,5),key='V'), sg.In(size=(5,5),key=22)],
#             [sg.Text('W'), sg.In(size=(5,5),key='W'), sg.In(size=(5,5),key=23)],
#             [sg.Text('X'), sg.In(size=(5,5),key='X'), sg.In(size=(5,5),key=24)],
#             [sg.Text('Y'), sg.In(size=(5,5),key='Y'), sg.In(size=(5,5),key=25)],
#             [sg.Text('Z'), sg.In(size=(5,5),key='Z'), sg.In(size=(5,5),key=26)]
#             ]

sg.theme_background_color(color='#00796B')

configuracion_letras = {
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

#COLUMNA DE LETRAS
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

#COLUMNA DEL INPUT DE CANTIDAD DE LETRAS
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

#COLUMNA DEL INPUT DEL VALOR DE LAS LETRAS
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
layout = [
            [sg.Column(colLet1), sg.Column(colCant1),sg.Column(colVal1),sg.Column(colLet2), sg.Column(colCant2),sg.Column(colVal2)],
            [sg.Button('Aplicar'), sg.Button('Salir')]
        ]



window = sg.Window('Configuracion de letras', layout)

while True:
    event, values = window.read()
    print(event)
    print(configuracion_letras)
    if event == 'Salir':
        break
    if event == 'Aplicar':
        print('Valores aplicados')

