import PySimpleGUI as sg
import random
import os
from coloresTablero import tablero_inicial
from images import *
from Tablero import Tablero



def main_game():

	obj_tablero = Tablero()
	obj_tablero.iniciar_tablero()
	
	tab=tablero_inicial(obj_tablero)
	sg.ChangeLookAndFeel('Dark purple')



	blank = {'letra':'', 'imagen': r'app/images/blank.png'}
	a={'letra':'A','imagen': r'app/images/a.png'} #(r'img.png')
	b={'letra':'B','imagen': r'app/images/b.png'}
	c={'letra':'C','imagen': r'app/images/c.png'}
	d={'letra':'D','imagen': r'app/images/d.png'}
	e={'letra':'E','imagen': r'app/images/e.png'}
	f={'letra':'F','imagen': r'app/images/f.png'}
	g={'letra':'G','imagen': r'app/images/g.png'}
	h={'letra':'H','imagen': r'app/images/h.png'}
	i={'letra':'I','imagen': r'app/images/i.png'}
	j={'letra':'J','imagen': r'app/images/j.png'}
	k={'letra':'K','imagen': r'app/images/k.png'}
	l={'letra':'L','imagen': r'app/images/l.png'}
	m={'letra':'M','imagen': r'app/images/m.png'}
	n={'letra':'N','imagen': r'app/images/n.png'}
	o={'letra':'O','imagen': r'app/images/o.png'}
	p={'letra':'P','imagen': r'app/images/p.png'}
	q={'letra':'Q','imagen': r'app/images/q.png'}
	r={'letra':'R','imagen': r'app/images/r.png'}
	s={'letra':'S','imagen': r'app/images/s.png'}
	t={'letra':'T','imagen': r'app/images/t.png'}
	u={'letra':'U','imagen': r'app/images/u.png'}
	v={'letra':'V','imagen': r'app/images/v.png'}
	w={'letra':'W','imagen': r'app/images/w.png'}
	x={'letra':'X','imagen': r'app/images/x.png'}
	y={'letra':'Y','imagen': r'app/images/y.png'}
	z={'letra':'Z','imagen': r'app/images/z.png'}
	im=r'app/images/g.png'
	img=r'app/images/blank2.png'####
	#b={'letra': 'B', 'imagen' : os.path_join(PATH, 'a.png')}
	# b={'letra':'A','imagen': os.path.join(PATH,'a.png')}
	# b={'letra':'B','imagen': os.path.join(PATH,'a.png')}
	# c={'letra':'C','imagen': os.path.join(PATH,'a.png')}
	# d={'letra':'D','imagen': os.path.join(PATH,'a.png')}
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
	for i in range(15):  ### tablero botones
		row=[]
		for j in range(15):
			#color_button=('white','white')
			color_button=('white','white')

			piece_image = images['BLANK']
			dd=tab[i][j]
			if dd['color']== 'red':
						
					color_button=('white','red')
					
					row.append(render_square(piece_image['imagen'],key = (i,j)))
			# elif dd['color']=='orange':
					# color_button=('white','blue')
					# row.append(render_square(piece_image['imagen'],key = (i,j)))			
			elif dd['color']=='violet':
					#corona=r'corona.png'
					color_button=('white','violet')
					corona=r'app/images/corona.png'
					row.append(render_square(corona,key = (i,j)))			
			elif dd['color']=='orange':
					color_button=('white',dd['color'])
					row.append(render_square(piece_image['imagen'],key = (i,j)))
					
			else:
				row.append(render_square(piece_image['imagen'],key = (i,j)))
				#row.append(sg.Button('palabraX3',key=(i,j))	
		tablero.append(row)
	color_button=('white','white')	
	#print(tablero)	
		
	## botones del atril

	atril = []
	atril2 = []
	for i in range(7):
		row = []
		piece_image = images[initial_atril[i]]
		row.append(render_square(piece_image['imagen'],key = i))
		atril.append(row)###	
		
	#print(atril)
	inte=r'app/images/interrogacion.png'
	for i in range(7):
		row = []
		#piece_image = images[initial_atril[i]]
		row.append(render_square(inte,key = i))
		atril2.append(row)###	
		
		
	board_tab=[[sg.Button('CHECK')],[sg.Text('PUNTOS JUGADOR'),sg.Text('0'),sg.Column(atril), sg.Column(tablero), sg.Column(atril2),sg.Text('PUNTOS MAQUINA'),sg.Text('0')],[sg.Button('COMENZAR'),sg.Button('EXIT'),sg.Button('PASAR')]]
	window = sg.Window('ScrabbleAr',default_button_element_size=(10,1), auto_size_buttons=False).Layout(board_tab)
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

