import PySimpleGUI as sg
import random
import os.path

import configuracion

base_path=os.path.dirname(os.path.abspath(__file__))


def main_game():
	boardConfig1=configuracion.Config1()


	
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
		
	class Tablero():
		
	
 		#sg.RButton(texto,image_size=(50, 50), pad=(2,2),key=key)

	
		def render_square(self, image ,key , texto= '',color_button=('white','white')):
		#return sg.RButton(texto,image_filename=image,image_size=(50, 50), pad=(2,2),key=key,button_color=color_button) 
		
			return sg.RButton(texto,image_filename=image,image_size=(50, 50), pad=(2,2),key=key,button_color=color_button)		



			
			
			
	class Tablero1(Tablero):
		def TableroFacil(self,images):
	
	
			tamaño=(50,50)
		
	
		
				
				
			tablero1=[]
			for i in range(15):
				row=[]
				for j in range(15):
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
						row.append(self.render_square(piece_image,key =(i,j),texto='', color_button=('white','green')))
			
					elif color == 'red':
						#piece_image=os.path.join(base_path,'images/P2.png')
						piece_image = images_PuntosNv1['PX3']
						row.append(self.render_square(piece_image,key =(i,j),texto='', color_button=('white','red')))
					elif color == 'blue':
						#piece_image=os.path.join(base_path,'images/PX2.png')
						piece_image = images_PuntosNv1['LX3']
						row.append(self.render_square(piece_image,key =(i,j),texto='', color_button=('white','blue')))
					elif color == 'violet':
						piece_image=os.path.join(base_path,'images/corona.png')
						row.append(self.render_square(piece_image,key =(i,j),texto='', color_button=('white','white')))												
					elif color == 'orange':
						#piece_image=os.path.join(base_path,'images/PX2.png')
						piece_image = images_PuntosNv1['PX2']
						row.append(self.render_square(piece_image,key =(i,j),texto='', color_button=('white','orange')))




						
					else:
						color_button=('white','white')
						row.append(self.render_square(piece_image['imagen'],key =(i,j),texto=''))
		
				tablero1.append(row)
		
			return (tablero1,tamaño)
			
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
				
					
					row.append(render1(img,key =(i),texto='', color_button=('white','white')))
					atril.append(row)
			return atril
			
	def modificarBoton(): 
		print(button)
		if boardConfig1[button[0]][button[1]].get_estado() == True:
			print('esta ocupado')
		else:
			
			img=''
			window[i].update(image_filename=img,image_size=(50, 50), button_color=('',''))
			
			
			piece_image = images[initial_atril[i]]
			img=piece_image['imagen']
			window[button].update(image_filename=img, image_size= tamaño_img ,button_color=('white','grey'))
			p2=palabra[0]
			p2=p2+letra
			palabra[0]=p2
			initial_atril[i]='' ## relacionar con la bolsa
			boardConfig1[button[0]][button[1]].set_estado(True)			

	def BorrarTablero(color):### algo que no  vi cuando estaba haciendo el tablero , es el hecho de blanquear el tablero cuando ocurra el evento pasar , si tengo 3 tablero debo repetir 3 veces este metodo 
		if color == 'green':
			piece_image = images_PuntosNv1['LX2']
			#row.append(self.render_square(piece_image,key =(i,j),texto='', color_button=('white','green')))
			window[(i,j)].update(image_filename=piece_image, image_size= tamaño_img ,button_color=('white','green'))
		
		elif color == 'red':
			piece_image = images_PuntosNv1['PX3']
			#row.append(self.render_square(piece_image,key =(i,j),texto='', color_button=('white','red')))
			

			window[(i,j)].update(image_filename=piece_image, image_size= tamaño_img ,button_color=('white','red'))
		elif color == 'blue':
			piece_image = images_PuntosNv1['LX3']
			#row.append(self.render_square(piece_image,key =(i,j),texto='', color_button=('white','blue')))
			window[(i,j)].update(image_filename=piece_image, image_size= tamaño_img ,button_color=('white','blue'))
		elif color == 'violet':
			piece_image=os.path.join(base_path,'images/corona.png')
			#row.append(self.render_square(piece_image,key =(i,j),texto='', color_button=('white','white')))
			window[(i,j)].update(image_filename=piece_image, image_size= tamaño_img ,button_color=('white','white'))												
		elif color == 'orange':
			piece_image = images_PuntosNv1['PX2']
			#row.append(self.render_square(piece_image,key =(i,j),texto='', color_button=('white','orange')))
			window[(i,j)].update(image_filename=piece_image, image_size= tamaño_img ,button_color=('white','orange'))
						
		else:
			#color_button=('white','white')
			piece_image = images['BLANK']
			piece_image = piece_image['imagen']
			#row.append(self.render_square(piece_image['imagen'],key =(i,j),texto='')) 
			window[(i,j)].update(image_filename=piece_image, image_size= tamaño_img ,button_color=('white','white'))
####################
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
	cantPasadas=0
	#palabra=''	
	
	palabra=['']
	i=0
	cant=0
	T1=True
	T2= True
	T3= True
	F=0
	C=0
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
		if button =='PASAR':
			cantPasadas=cantPasadas+1
			if cantPasadas<4:
				print('dd')
				initial_atril=[]
				for i in range(0,7): ##cambiar i
					initial_atril.append(random.choice(images_keys))
				for i in range(7):
					#window[i].update(initial_atril[i])
					piece_image = images[initial_atril[i]]
									
					img=piece_image['imagen']

					window[i].update(image_filename=img,image_size=(50, 50), button_color=('',''))
		##### blanquear tablero
				for i in range(10):
					for j in range(10):
						window[(i,j)].update('')
						boardConfig1[i][j].set_estado(False)
						color=boardConfig1[i][j].get_color()
						BorrarTablero(color)
			cant=0
			T1=True
			T2=True
			palabra=['']
	
				
			
				
		if type(button) is int:
			print(button)
			
			if initial_atril[button] !='':
				i=button
				letra= initial_atril[button]
				#####hoy palabra += letra

				button , value = window.Read()
				if type(button) is tuple:
					if (button[0]==7 and button[1]==7)and T3:
						print(button)
						modificarBoton()
						T3=False
						F=button[0]
						C=button[1]
					#print(type(lista[1]))
					if not(T3):
						if(button[0]==F)and T1:
							if C<button[1]:
								T2=False
								modificarBoton()
								C=button[1]
						if(button[1]==C)and T2:
							if F<button[0]:
								print(button)
								T1=False
								modificarBoton()
								F=button[0]	
				
					l=0
	
			
			
		if type(button) is tuple:
			if l ==-1:
				
				sg.Popup('movimiento incorrecto')			
			
			
			


main_game()
