import PySimpleGUI as sg
import random
import os.path

import ConfigColorPunt

base_path=os.path.dirname(os.path.abspath(__file__))


def main_game():

	
	blank = {'letra':'', 'imagen': os.path.join(base_path,'images/fondo.png')}
	a={'letra':'A','imagen': os.path.join(base_path,'images/a.png')} #(r'img.png')
	b={'letra':'B','imagen': os.path.join(base_path,'images/b.png')}
	c={'letra':'C','imagen': os.path.join(base_path,'images/c.png')}
	d={'letra':'D','imagen': os.path.join(base_path,'images/d.png')}
	e={'letra':'E','imagen': os.path.join(base_path,'images/e.png')}
	f={'letra':'F','imagen': os.path.join(base_path,'images/f.png')}
	g={'letra':'G','imagen': os.path.join(base_path,'images/g.png')}
	h={'letra':'H','imagen': os.path.join(base_path,'images/h.png')}
	i={'letra':'I','imagen': os.path.join(base_path,'images/i.png')}
	j={'letra':'J','imagen': os.path.join(base_path,'images/j.png')}
	k={'letra':'K','imagen': os.path.join(base_path,'images/k.png')}
	l={'letra':'L','imagen': os.path.join(base_path,'images/l.png')}
	m={'letra':'M','imagen': os.path.join(base_path,'images/m.png')}
	n={'letra':'N','imagen': os.path.join(base_path,'images/n.png')}
	o={'letra':'O','imagen': os.path.join(base_path,'images/o.png')}
	p={'letra':'P','imagen': os.path.join(base_path,'images/p.png')}
	q={'letra':'Q','imagen': os.path.join(base_path,'images/q.png')}
	r={'letra':'R','imagen': os.path.join(base_path,'images/r.png')}
	s={'letra':'S','imagen': os.path.join(base_path,'images/s.png')}
	t={'letra':'T','imagen': os.path.join(base_path,'images/t.png')}
	u={'letra':'U','imagen': os.path.join(base_path,'images/u.png')}
	v={'letra':'V','imagen': os.path.join(base_path,'images/v.png')}
	w={'letra':'W','imagen': os.path.join(base_path,'images/w.png')}
	x={'letra':'X','imagen': os.path.join(base_path,'images/x.png')}
	y={'letra':'Y','imagen': os.path.join(base_path,'images/y.png')}
	z={'letra':'Z','imagen': os.path.join(base_path,'images/z.png')}
	px2=os.path.join(base_path,'images/PX2.png')
	lx3=os.path.join(base_path,'images/LX3.png')
	lx2=os.path.join(base_path,'images/LX2.png')
	px3=os.path.join(base_path,'images/PX3.png')
	images_PuntosNv1={'PX2':px2 , 'LX3':lx3 , 'LX2' :lx2 ,'PX3':px3}



	color_button=('white','white')
	images = {'BLANK':blank,'A': a, 'B': b, 'C': c, 'D': d, 'E': e, 'F': f, 'G': g, 'H': h, 'I': i, 'J': j, 'K': k, 'L': l, 'M': m, 'N': n, 'O': o, 'P': p, 'Q': q, 'R': r, 'S': s, 'T': t, 'U': u, 'V': v, 'W': w, 'X': x, 'Y': y, 'Z': z}
	initial_atril=[]
	images_keys= list(images.keys())
	images_keys.remove('BLANK')


	for i in range(0,7):
		initial_atril.append(random.choice(images_keys))	
	
	
	class Tablero:
		def __init__(self,filas,columnas):
			self._filas = filas
			self._columnas = columnas


		
	class Tablero1(Tablero):
		
		def __init__(self):
			super().__init__(15,15)
		def TableroFacil(self,images):
			tamaño=(50,50)
		
	
			boardConfig1=ConfigColorPunt.Config1()
			def render_square(image, key, texto='',color_button=('white','white'), tamaño_img=(50,50)):
				return sg.RButton(texto,image_filename=image,image_size=tamaño_img , pad=(2,2),key=key,button_color=color_button) ### consultar profe
			tablero1=[]
			for i in range(self._filas):
				row=[]
				for j in range(self._columnas):
					piece_image = images['BLANK']
					valor=boardConfig1[i][j].get_valor()
					color=boardConfig1[i][j].get_color()
					# if color == 'violet':
						# piece_image=os.path.join(base_path,'images/corona.png')
						# row.append(render_square(piece_image,key =(i,j),texto='', color_button=('white','Dark violet')))
						

					# elif valor == 2:
						# piece_image=os.path.join(base_path,'images/P2.png')
						# row.append(render_square(piece_image,key =(i,j),texto='', color_button=('white','orange')))
					if color == 'green':
						#piece_image=os.path.join(base_path,'images/PX2.png')
						piece_image = images_PuntosNv1['LX2']
						row.append(render_square(piece_image,key =(i,j),texto='', color_button=('white','green')))
						print(valor)
						print(color)
						print(i,j)
					elif color == 'red':
						#piece_image=os.path.join(base_path,'images/P2.png')
						piece_image = images_PuntosNv1['PX3']
						row.append(render_square(piece_image,key =(i,j),texto='', color_button=('white','red')))
					elif color == 'blue':
						#piece_image=os.path.join(base_path,'images/PX2.png')
						piece_image = images_PuntosNv1['LX3']
						row.append(render_square(piece_image,key =(i,j),texto='', color_button=('white','blue')))
					elif color == 'violet':
						piece_image=os.path.join(base_path,'images/corona.png')
						row.append(render_square(piece_image,key =(i,j),texto='', color_button=('white','white')))												
					elif color == 'orange':
						#piece_image=os.path.join(base_path,'images/PX2.png')
						piece_image = images_PuntosNv1['PX2']
						row.append(render_square(piece_image,key =(i,j),texto='', color_button=('white','orange')))




						
					else:
						color_button=('white','white')
						row.append(render_square(piece_image['imagen'],key =(i,j),texto=''))
		
				tablero1.append(row)
		
			return (tablero1,tamaño)	

	class Tablero2(Tablero):
		
		def __init__(self):
			super().__init__(7,7)
		def TableroMedio(self,images):
			
			boardConfig1=ConfigColorPunt.Config1()
			def render_square(image, key, texto='',color_button=('white','white')):
				return sg.RButton(texto,image_filename=image,image_size=(40, 40), pad=(2,2),key=key,button_color=color_button)
			tablero1=[]
			for i in range(self._filas):
				row=[]
				for j in range(self._columnas):
					piece_image = images['A']
					valor=boardConfig1[i][j].get_valor()
					if valor == 3:
						row.append(render_square(piece_image['imagen'],key =(i,j),texto='', color_button=('white','orange')))
					
					else:
						color_button=('white','white')
						row.append(render_square(piece_image['imagen'],key =(i,j),texto=''))
		
				tablero1.append(row)
		
			return tablero1	
			
	class Tablero3(Tablero):
		
		def __init__(self):
			super().__init__(7,7)
		def TableroDificil(self,images):
			
			boardConfig1=ConfigColorPunt.Config1()
			def render_square(image, key, texto='',color_button=('white','white')):
				return sg.RButton(texto,image_filename=image,image_size=(40, 40), pad=(2,2),key=key,button_color=color_button)
			tablero1=[]
			for i in range(self._filas):
				row=[]
				for j in range(self._columnas):
					piece_image = images['A']
					valor=boardConfig1[i][j].get_valor()
					if valor == 3:
						row.append(render_square(piece_image['imagen'],key =(i,j),texto='', color_button=('white','orange')))
					
					else:
						color_button=('white','white')
						row.append(render_square(piece_image['imagen'],key =(i,j),texto=''))
		
				tablero1.append(row)
		
			return tablero1				
			
			
			
			

	class atril1():
		def __init__(self,T=True):
			self._T= T
		def crearAtril(self):
			def render1(image, key, texto='',color_button=('white','white')):
				return sg.RButton(texto,image_filename=image,image_size=(50, 50), pad=(2,2),key=key,button_color=color_button)
			atril=[]
			
			if self._T:
				
				for i in  range(7):
					row=[]
					piece_image = images[initial_atril[i]]
					row.append(render1(piece_image['imagen'],key =(i),texto='', color_button=('white','white')))
					atril.append(row)
				
			else:
				img=os.path.join(base_path,'images/interrogacion.png')
				for i in  range(7):
					row=[]
					#piece_image = images['C']
					
					row.append(render1(img,key =(i),texto='', color_button=('white','white')))
					atril.append(row)
			return atril
			
			





	atr1=atril1(True).crearAtril()
	atr2=atril1(False).crearAtril()				
	obj = Tablero1()
	print('*')


	elementos=obj.TableroFacil(images) 
	tablero= elementos[0]
	tamaño_img = elementos[1]

	columna_3 = [ [sg.Text('PUNTOS MAQUINA')],[sg.Listbox(values =[], key='datosj', size=(30,10))]]
	columna_1 = [ [sg.Text('PUNTOS JUGADOR')],[sg.Listbox(values =[], key='datosm', size=(30,10))]]		
	


	board_tab=[[sg.Button('CHECK')],[sg.Column(columna_1),sg.Column(atr1),sg.Column(tablero),sg.Column(atr2),sg.Column(columna_3)],[sg.Button('COMENZAR'),sg.Button('PASAR'),sg.Button('GUARDAR'),sg.Button('EXIT')]]
	window = sg.Window('ScrabbleAr',default_button_element_size=(10,1), auto_size_buttons=False).Layout(board_tab)
	
	palabra=''	
	while True:
		letra=''
		l=-1
		button , value = window.Read()
		if button == 'CHECK':
			#obj_tablero.get_word()
			if palabra == '':
				sg.Popup('todavia no formo una palabra')
			else:
				print(palabra)
				sg.Popup('PALABRA FORMADA : ' ,palabra)
			# if len(word)>= 2 and len(word) <=7:
		if button in (None , 'EXIT'):
			exit()
				
		if type(button) is int:
			print(button)
			
			if initial_atril[button] !='':
				letra= initial_atril[button]
				palabra += letra


				initial_atril[button]='' ##
				img=''
				#window[button].update(image_filename=img, button_color=('',''))##
				window[button].update(image_filename=img,image_size=(50, 50), button_color=('',''))
				button , value = window.Read()
				if type(button) is tuple:
		
					image1= images[letra]
					image1=image1['imagen']
					#imgT=(50,50)
			
					#render_square(image1['imagen'],key=(0,0))
					window[button].update(image_filename=image1, image_size= tamaño_img ,button_color=('white','grey')) ###  si no agreggo el tamaño el boton toma el tamaño de la imagen
					# se modifica la letra en el tablero
					# obj_tablero.change_letra(button[0],button[1],letra)				
					l=0
				# piece_image = images['BLANK']
			# row.append(render_square(piece_image['imagen'],key = (i,j)))	
			
			
			
		if type(button) is tuple:
			if l ==-1:
				
				sg.Popup('movimiento incorrecto')







main_game()		
		
		
		
		
		


