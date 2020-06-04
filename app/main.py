import PySimpleGUI as sg
import random
import os
from images import *
from Tablero import Tablero
sg.ChangeLookAndFeel('Dark purple')
## disculpen la demora por subir el codigo , en la  semana voy a estar modificanco este tablero agregando modulos y objetos para que el codigo sea mas organizado
## hoy voy a tratar de implementar el patron de colores 
obj_tablero = Tablero()
obj_tablero.iniciar_tablero()

blank = {'letra':'', 'imagen': os.sep.join(['app/images', 'blank.png'])}
a={'letra':'A','imagen': os.sep.join(['app/images', 'a.png'])} #(r'img.png'])
b={'letra':'B','imagen': os.sep.join(['app/images', 'b.png'])}
c={'letra':'C','imagen': os.sep.join(['app/images', 'c.png'])}
d={'letra':'D','imagen': os.sep.join(['app/images', 'd.png'])}
e={'letra':'E','imagen': os.sep.join(['app/images', 'e.png'])}
f={'letra':'F','imagen': os.sep.join(['app/images', 'f.png'])}
g={'letra':'G','imagen': os.sep.join(['app/images', 'g.png'])}
h={'letra':'H','imagen': os.sep.join(['app/images', 'h.png'])}
i={'letra':'I','imagen': os.sep.join(['app/images', 'i.png'])}
j={'letra':'J','imagen': os.sep.join(['app/images', 'j.png'])}
k={'letra':'K','imagen': os.sep.join(['app/images', 'k.png'])}
l={'letra':'L','imagen': os.sep.join(['app/images', 'l.png'])}
m={'letra':'M','imagen': os.sep.join(['app/images', 'm.png'])}
n={'letra':'N','imagen': os.sep.join(['app/images', 'n.png'])}
o={'letra':'O','imagen': os.sep.join(['app/images', 'o.png'])}
p={'letra':'P','imagen': os.sep.join(['app/images', 'p.png'])}
q={'letra':'Q','imagen': os.sep.join(['app/images', 'q.png'])}
r={'letra':'R','imagen': os.sep.join(['app/images', 'r.png'])}
s={'letra':'S','imagen': os.sep.join(['app/images', 's.png'])}
t={'letra':'T','imagen': os.sep.join(['app/images', 't.png'])}
u={'letra':'U','imagen': os.sep.join(['app/images', 'u.png'])}
v={'letra':'V','imagen': os.sep.join(['app/images', 'v.png'])}
w={'letra':'W','imagen': os.sep.join(['app/images', 'w.png'])}
x={'letra':'X','imagen': os.sep.join(['app/images', 'x.png'])}
y={'letra':'Y','imagen': os.sep.join(['app/images', 'y.png'])}
z={'letra':'Z','imagen': os.sep.join(['app/images', 'z.png'])}
im= os.sep.join(['app/images', 'g.png'])
img= os.sep.join(['app/images', 'blank2.png'])####
#b={'letra': 'B', 'imagen' : os.path_join(sep, 'a.png'])}
# b={'letra':'A','imagen': os.sep.join(sep,'a.png'])}
# b={'letra':'B','imagen': os.sep.join(sep,'a.png'])}
# c={'letra':'C','imagen': os.sep.join(sep,'a.png'])}
# d={'letra':'D','imagen': os.sep.join(sep,'a.png'])}
color_button=('white','white')
images = {'BLANK':blank,'A': a, 'B': b, 'C': c, 'D': d, 'E': e, 'F': f, 'G': g, 'H': h, 'I': i, 'J': j, 'K': k, 'L': l, 'M': m, 'N': n, 'O': o, 'P': p, 'Q': q, 'R': r, 'S': s, 'T': t, 'U': u, 'V': v, 'W': w, 'X': x, 'Y': y, 'Z': z}

initial_atril=[]
images_keys= list(images.keys())
images_keys.remove('BLANK')


for i in range(0,7):
	initial_atril.append(random.choice(images_keys))


def render_square(image, key):
	return sg.RButton('',image_filename=image, size=(2,2), pad=(2,2),key=key,button_color=color_button)
	
tablero=[]
for i in range(10):  ### tablero botones
	row=[]
	for j in range(10):
		piece_image = images['BLANK']
		row.append(render_square(piece_image['imagen'],key = (i,j)))	
	tablero.append(row)
	
	
#print(tablero)	
	
## botones del atril

atril = []
for i in range(7):
	row = []
	piece_image = images[initial_atril[i]]
	row.append(render_square(piece_image['imagen'],key = i))
	atril.append(row)###	
	
#print(atril)	
	
board_tab=[[sg.Button('CHECK')],[sg.Column(atril), sg.Column(tablero)],[sg.Button('COMENZAR'),sg.Button('PASAR'),sg.Button('EXIT')]]
window = sg.Window('ScrabbleAr',default_button_element_size=(10,2), auto_size_buttons=False, icon='ScrabbleGO.ico').Layout(board_tab)
#indow = sg.Window('tablero', layout, default_button_element_size=(5,2), auto_size_buttons=False)
#event, value = window.Read()
palabra=''
while True:
	letra=''
	l=-1
	button , value = window.Read()
	if button == 'CHECK':
		obj_tablero.get_word()
		if palabra == '':
			sg.Popup('todavia no formo una palabra')
		else:
		    print(palabra)
		# if len(word)>= 2 and len(word) <=7:
	if button in (None , 'EXIT'):
		exit()		
	if type(button) is int:
		if initial_atril[button] !='':
			letra= initial_atril[button]
			palabra += letra
		
			initial_atril[button]=''
			window[button].update(image_filename=img, button_color=('',''))##
			button , value = window.Read()
			if type(button) is tuple:
				
				image1= images[letra]
				image1=image1['imagen']
				
				#render_square(image1['imagen'],key=(0,0))
				window[button].update(image_filename=image1, button_color=('white','grey'))

				# se modifica la letra en el tablero
				obj_tablero.change_letra(button[0],button[1],letra)
				
				l=0
			# piece_image = images['BLANK']
		# row.append(render_square(piece_image['imagen'],key = (i,j)))	
	
		
		
	if type(button) is tuple:
		if l ==-1:
			
			sg.Popup('movimiento incorrecto')
