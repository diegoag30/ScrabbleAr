import PySimpleGUI as sg
import random
from itertools import combinations
import time
import clasificarPalabra
import IA
import os.path
import config_tablero
from Bolsa import Bolsa
from Configuracion import Configuracion

base_path=os.path.dirname(os.path.abspath(__file__))
"""
 gestiona todas las operacions necesarias para generar el tablero  y modificar su estado 
."""
def main_game(num_tablero, configuracion):
	
	#Inicializacion de variables e imagenes
	conf = configuracion
	bolsa = Bolsa(conf.getConfiguracionLetras())
	PC=IA
	clasificar=clasificarPalabra

	"""
	  ruta absaluta para utilizar recursos
	."""

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
	
	"""
	 son los diccionarios que contienen las imagenes  para cada tablero del juego
	."""  	
	images_PuntosTablero2={'centro':os.path.join(base_path,'images/centro.png'), 'fondo':os.path.join(base_path,'images/fond2.png'), 'green' :os.path.join(base_path,'images/LX2.png') ,'red':os.path.join(base_path,'images/PX3.png'),'orange':os.path.join(base_path,'images/PX-2.png'),'blue':os.path.join(base_path,'images/LX3.png')}
	images_PuntosTablero3={'centro':os.path.join(base_path,'images/corona1.png'),'fondo':os.path.join(base_path,'images/fond3.png'),'red':os.path.join(base_path,'images/PX3ESC.png'),'orange':os.path.join(base_path,'images/PX2ESC.png'),'blue':os.path.join(base_path,'images/LX-3Cr.png'),'green':os.path.join(base_path,'images/LX-2Cr.png')}
	images_PuntosTablero1={'centro':os.path.join(base_path,'images/corona.png'),'fondo':os.path.join(base_path,'images/fondo.png'),'red':os.path.join(base_path,'images/PX3.png'),'orange':os.path.join(base_path,'images/PX2.png'),'blue':os.path.join(base_path,'images/LX3.png'),'green':os.path.join(base_path,'images/LX2.png')}	
	images_PuntosTablero={}
	fichasIA=[]
	color_button=('white','white')
	images = {'BLANK':blank,'A': a, 'B': b, 'C': c, 'D': d, 'E': e, 'F': f, 'G': g, 'H': h, 'I': i, 'J': j, 'K': k, 'L': l, 'M': m, 'N': n, 'O': o, 'P': p, 'Q': q, 'R': r, 'S': s, 'T': t, 'U': u, 'V': v, 'W': w, 'X': x, 'Y': y, 'Z': z}


	images_keys= list(bolsa.letras_validas().keys()) ### Se recibe las letras configuradas por el usuario, y se eliminan las que estan en 0
	

	random.shuffle(images_keys,random.random)
	initial_atril=[]
	initial_atril2=[]
	PC.atrilPalabrasValidas(images_keys,initial_atril2, conf)
	initial_atril=initial_atril2[:]


	## SE Restan las fichas cuando se crea el atril del jugador, ademas se quitan las fichas que quedaron en 0
	for ficha in initial_atril:
		if ficha in bolsa.get_fichas():
			bolsa.quitar_fichas(ficha,1)
	images_keys = list(bolsa.letras_validas().keys())
	#print(bolsa.letras_validas().keys())

	def actualizar_layout_bolsa():
		for ficha in bolsa.get_fichas().keys():
			window.FindElement(ficha).update(bolsa.cant_letras(ficha))


	def get_name():
		'''Pop up inicial, que obtiene el nombre del jugador, para poder agregarlo al ranking en caso de ser necesario '''
		layout = [[sg.Text('Bienvenido a ScrabbleAR. Por favor introduce tu nombre:',background_color='#00796B'),],      
					[sg.InputText(key='-IN-')],      
					[sg.Submit(), sg.Cancel()]]      

		window = sg.Window('Window Title', layout)    
		event, values = window.read()    
		window.close()
		text_input = values['-IN-']
		return text_input  

	"""
	 clase padre que hereda un metodo para generar botones 
	."""
	class Tablero():
		
	
 		

	
		def render_square(self, image ,key , texto= '',color_button=('white','white')):
		#return sg.RButton(texto,image_filename=image,image_size=(50, 50), pad=(2,2),key=key,button_color=color_button) 
		
			return sg.RButton(texto,image_filename=image,image_size=(50, 50), pad=(2,2),key=key,button_color=color_button)		


	"""
	 genera los tres tablero necesarios para el juego 
	 segun una configuaracion dada por un objeto (boardConfig) se contiene el estado segun el tablero que se pida 
	.""" 
			
			
			
	class Tablero(Tablero):
		def Tab(self,images):
	
	
			tamaño=(50,50)
			tablero1=[]
			for i in range(15):
				row=[]
				for j in range(15):
				
					piece_image=images_PuntosTablero['fondo']
					valor=boardConfig[i][j].get_valor()
					color=boardConfig[i][j].get_color()
	
					if color == 'green':
		
						piece_image=images_PuntosTablero['green']
						row.append(self.render_square(piece_image,key =(i,j),texto='', color_button=('white','green')))
			
					elif color == 'red':
				
						piece_image=images_PuntosTablero['red']
						row.append(self.render_square(piece_image,key =(i,j),texto='', color_button=('white','red')))
					elif color == 'blue':
					
						piece_image=images_PuntosTablero['blue']
						row.append(self.render_square(piece_image,key =(i,j),texto='', color_button=('white','blue')))
					elif color == 'violet':
						#piece_image=os.path.join(base_path,'images/corona.png')
						piece_image=images_PuntosTablero['centro']
						
						row.append(self.render_square(piece_image,key =(i,j),texto='', color_button=('white','Dark violet')))												
					elif color == 'orange':
						#piece_image=os.path.join(base_path,'images/PX2.png')
						#piece_image = images_PuntosNv1['PX2']
						piece_image=images_PuntosTablero['orange']
						row.append(self.render_square(piece_image,key =(i,j),texto='', color_button=('white','orange')))




						
					else:
						color_button=('white','white')
						row.append(self.render_square(piece_image,key =(i,j),texto=''))
		
				tablero1.append(row)
		
			return (tablero1,tamaño)
		
	""" genera dos atriles que contienen las palabras del jugador y de simbolos que representan las palabras de la  pc  ."""			

			
	class atril1():
		'''Clase que controla la UI del '''
		def __init__(self,T=True):
			self._T= T
		def crearAtril(self):
			def render1(image, key, texto='',color_button=('white','white')):
				return sg.RButton(texto,image_filename=image,image_size=(50, 50), pad=(2,2),key=key,button_color=color_button)
			atril=[]
			#Si se pasa true como parametro, los botones del atril se rellenan con letras
			if self._T: 
				
				for i in  range(7):
					row=[]
					piece_image = images[initial_atril[i]]
					row.append(render1(piece_image['imagen'],key =(i),texto='', color_button=('white','white')))
					atril.append(row)
			#En caso de que se pase false, se mostraran signos de interrogacion en el atril(atril de la computadora)	
			else: 
				img=os.path.join(base_path,'images/interrogacion.png')
				for i in  range(7):
					row=[]
				
					
					row.append(render1(img,key =(i),texto='', color_button=('white','white')))
					atril.append(row)
			return atril


	def modificarBoton(valores): 
		''' modificartBoton () cambia el estado del boton , cambia la imagen de una pieza del tablero y consta que esta ocupado'''
		#if boardConfig[button[0]][button[1]].get_estado() == True:
			#print('')

		if boardConfig[button[0]][button[1]].get_estado() == False:
			img=''
			window[i].update(image_filename=img,image_size=(50, 50), button_color=('',''))
			valores.append(boardConfig[button[0]][button[1]].get_valor())
			
			piece_image = images[initial_atril[i]]
			img=piece_image['imagen']
			window[button].update(image_filename=img, image_size= tamaño_img ,button_color=('white','grey'))
			listadoPosicionLetrasTablero.append(button)
			p2=palabra[0]
			p2=p2+letra
			palabra[0]=p2
			initial_atril[i]='' ## relacionar con la bolsa
			listadoPosicionLetrasAtril.append(i)
			boardConfig[button[0]][button[1]].set_estado(True)
		print('los valores de las letras son: ', valores)

			
		

	""" devuelve las letras ivalidas ingresadas en el tablero al atril respetando el orden en que fueron ingresadas ."""


	def devolverLetras():
		
		#images_PuntosTablero3
		p=palabra[0]
		print(p)
		cont=0		
		#if opc==3:
			
		for i in listadoPosicionLetrasAtril:
			piece_image = images[p[cont]]
			img=piece_image['imagen']
			window[i].update(image_filename=img,image_size=(50, 50), button_color=('',''))
			initial_atril[i]=p[cont]
			
			img=images_PuntosTablero['fondo']
		
			
			boardConfig[listadoPosicionLetrasTablero[cont][0]][listadoPosicionLetrasTablero[cont][1]].set_estado(False)
			#color=boardConfig[listadoPosicionLetrasTablero[cont][0][listadoPosicionLetrasTablero[cont][1]].get_color()
			color=boardConfig[listadoPosicionLetrasTablero[cont][0]][listadoPosicionLetrasTablero[cont][1]].get_color()
			if color == 'violet':
				piece_image=images_PuntosTablero['centro']
				
				window[listadoPosicionLetrasTablero[cont]].update(image_filename=piece_image, image_size= tamaño_img ,button_color=('white','Dark violet'))
			elif color == 'green':
				piece_image=images_PuntosTablero['green']
					
				window[listadoPosicionLetrasTablero[cont]].update(image_filename=piece_image, image_size= tamaño_img ,button_color=('white','green'))					
			elif color == 'red':									
				piece_image=images_PuntosTablero['red']
					
				window[listadoPosicionLetrasTablero[cont]].update(image_filename=piece_image, image_size= tamaño_img ,button_color=('white','red'))	
			elif color == 'blue':									
				piece_image=images_PuntosTablero['blue']
					
				window[listadoPosicionLetrasTablero[cont]].update(image_filename=piece_image, image_size= tamaño_img ,button_color=('white','blue'))					
			elif color == 'orange':									
				piece_image=images_PuntosTablero['orange']
					
				window[listadoPosicionLetrasTablero[cont]].update(image_filename=piece_image, image_size= tamaño_img ,button_color=('white','orange'))

								
			else:
				window[listadoPosicionLetrasTablero[cont]].update(image_filename=img, image_size= tamaño_img ,button_color=('white','white'))
			cont=cont+1

		print(initial_atril)											
	"""actualiza el atril del jugador despues de comprobar que la palabra ingresada es correcta con el boton Check."""
	def actualizarAtrilJugador():
		initial_atril2=[]
		random.shuffle(images_keys,random.random)
		PC.atrilPalabrasValidas(images_keys,initial_atril2, conf)
			
		for i in range(0,7):
			if initial_atril[i]=='':
				# initial_atril[i]=random.choice(initial_atril2)
				initial_atril[i]=initial_atril2[i]
				piece_image = images[initial_atril[i]]
				img=piece_image['imagen']
				window[i].update(image_filename=img,image_size=(50, 50), button_color=('',''))
		print(initial_atril)
							
	""" actualiza el atril y limpia del tablero las palabras ingresadas en se turno ."""
	def PasarTurno(initial_atril):
		if len(listadoPosicionLetrasTablero)>0:
			

				
			for i in range(0,len(listadoPosicionLetrasTablero)):
				img=images_PuntosTablero['fondo']	
				boardConfig[listadoPosicionLetrasTablero[i][0]][listadoPosicionLetrasTablero[i][1]].set_estado(False)
				#color=boardConfig[listadoPosicionLetrasTablero[cont][0][listadoPosicionLetrasTablero[cont][1]].get_color()
				color=boardConfig[listadoPosicionLetrasTablero[i][0]][listadoPosicionLetrasTablero[i][1]].get_color()
				if color == 'violet':
					piece_image=images_PuntosTablero['centro']
					
					window[listadoPosicionLetrasTablero[i]].update(image_filename=piece_image, image_size= tamaño_img ,button_color=('white','Dark violet'))	
				elif color == 'green':
					piece_image=images_PuntosTablero['green']
						
					window[listadoPosicionLetrasTablero[i]].update(image_filename=piece_image, image_size= tamaño_img ,button_color=('white','green'))					
				elif color == 'red':									
					piece_image=images_PuntosTablero['red']
						
					window[listadoPosicionLetrasTablero[i]].update(image_filename=piece_image, image_size= tamaño_img ,button_color=('white','red'))	
				elif color == 'blue':									
					piece_image=images_PuntosTablero['blue']
						
					window[listadoPosicionLetrasTablero[i]].update(image_filename=piece_image, image_size= tamaño_img ,button_color=('white','blue'))					
				elif color == 'orange':									
					piece_image=images_PuntosTablero['orange']
						
					window[listadoPosicionLetrasTablero[i]].update(image_filename=piece_image, image_size= tamaño_img ,button_color=('white','orange'))
	
									
				else:
					window[listadoPosicionLetrasTablero[i]].update(image_filename=img, image_size= tamaño_img ,button_color=('white','white'))
				
									
							
		print(initial_atril,'xxx inicio')
		initial_atril2=[]
		random.shuffle(images_keys,random.random)

		PC.atrilPalabrasValidas(images_keys,initial_atril2, conf)
		initial_atril=[]
		print(initial_atril2,'xxxx2')
		print(initial_atril,'xxxx1')
		#initial_atril2=[]
		print(initial_atril2,'xxxx2')
		
		initial_atril=initial_atril2[:]
		print(initial_atril,'Final')
	
		for i in range(7):
			#window[i].update(initial_atril[i])
			piece_image = images[initial_atril[i]]
							
##### blanquear tablero
			img=piece_image['imagen']

			window[i].update(image_filename=img,image_size=(50, 50), button_color=('',''))				
				
							
		return initial_atril			

	""" cada vez que se termine una partida  se limpia del tablero todas las palabras ingresadas ."""

	def BorrarTablerGeneral():
		def BorrarTablero(color):
			piece_image=images_PuntosTablero['fondo']		
		
			if color == 'green':
				piece_image=images_PuntosTablero['green']
		
			

				window[(i,j)].update(image_filename=piece_image, image_size= tamaño_img ,button_color=('white','green'))
		
			elif color == 'red':
				piece_image=images_PuntosTablero['red']
				

			
	
				window[(i,j)].update(image_filename=piece_image, image_size= tamaño_img ,button_color=('white','red'))
			elif color == 'blue':
			
			    piece_image=images_PuntosTablero['blue']
		
			    window[(i,j)].update(image_filename=piece_image, image_size= tamaño_img ,button_color=('white','blue'))
			elif color == 'violet':
			
			    piece_image=images_PuntosTablero['centro']
			
			    window[(i,j)].update(image_filename=piece_image, image_size= tamaño_img ,button_color=('white','Dark violet'))												
			elif color == 'orange':
		
			    piece_image=images_PuntosTablero['orange']
			
			    window[(i,j)].update(image_filename=piece_image, image_size= tamaño_img ,button_color=('white','orange'))
						
			else:
 
			   window[(i,j)].update(image_filename=piece_image, image_size= tamaño_img ,button_color=('white','white'))		

		
		for i in range(15):
			for j in range(15):
				window[(i,j)].update('')
				boardConfig[i][j].set_estado(False)
				color=boardConfig[i][j].get_color()
				BorrarTablero(color)	



	""" actualizad el listado que contiene el historial de casillas con premios del jugador y la PC."""	
			
	def actualizar_listado(listbox):
		listbox.Update(listado)	## accedo a la tupla			
	"""se crea el atril del jugador y la Pc."""	

####################
	#inteligencia1.saludo()
	nombre = get_name()
	word_values = []
	print(nombre)
	atr1=atril1(True).crearAtril()
	atr2=atril1(False).crearAtril()
	""" en base a una opcion ingresada por la configuracion se instancia un objeto tablero y se elige una configuracion para crear el tablero."""		
	if num_tablero ==1:

		images_PuntosTablero=images_PuntosTablero1
		
		boardConfig=config_tablero.Config1()
		obj = Tablero()
		opc=1
	elif num_tablero == 2:
		#obj = Tablero2()
		images_PuntosTablero=images_PuntosTablero2
		boardConfig=config_tablero.Config2()
		obj = Tablero()	
		#opc=2	
	elif num_tablero ==3:
		images_PuntosTablero=images_PuntosTablero3
		boardConfig=config_tablero.Config3()
		obj = Tablero()
	#bolsa.sacar_fichas(14)		


	""""""""""""""""""""""" interfaz grafica del tablero    ."""""""""""""""""""""

	elementos=obj.Tab(images) ##### estaria para conectarlo con una opcion para elegir el tablero
	tablero= elementos[0] 
	tamaño_img = elementos[1]
	columna_2 = [ [sg.Text('PUNTOS MAQUINA')],[sg.Listbox(values =[], key='datosm', font='Courier 18' ,size=(20,10))],[sg.Text('TOTAL PUNTOS')],[sg.Column(bolsa.get_layout(),key="BOLSA")]]
	columna_1 = [ [sg.Text('PUNTOS JUGADOR')],[sg.Listbox(values =[], key='datosj', font='Courier 18',size=(20,10))],[sg.Text('TOTAL PUNTOS')],[sg.Text('00:00:00', background_color=('#01a9b4'),key='reloj')]]

	columna_3 = [ [sg.Text('Total Puntos')]]

					
		
	"""se agregar las  columnas a una estructura que esta contenida dentro del layout."""

	board_tab=[[sg.Button('CHECK',disabled=True)],[sg.Column(columna_1), sg.Column(atr1),sg.Column(tablero),sg.Column(atr2),sg.Column(columna_2)],[sg.Button('COMENZAR',button_color=('white','green')),sg.Button('PASAR',disabled=True),sg.Button('GUARDAR',disabled=True),sg.Button('EXIT')]]
	window = sg.Window('ScrabbleAr',default_button_element_size=(12,1), auto_size_buttons=False).Layout(board_tab)
	cantPasadas=0
	#palabra=''	
	controlAt=[7,7,0,0]

	palabra=['']
	#i=0
	""" condicionales para elegir y seguir una orientacion  , para las palabras del jugador ."""		
	cant=2
	T1=True
	T2= True
	T3= True
	T4= True
	F=0
	C=0
	#x=0
	puntosCasilla=[]
	putosL=0
	"""listas necesarias para controlar el estado de las palabras ingresadas al tablero ."""	
	
	listadoPosicionLetrasAtril=[]
	listadoPosicionLetrasTablero=[]
	listadoPc=[]
	listado=[]
	#inicio=time.time()
	wait=True
	wait2=True
	window.Finalize()
	""" temporizador del juego."""		
	inicio=time.time()
	iniciar=True
	puntaje_jugador = 0
	

	while ((True and iniciar)and (not bolsa.bolsa_vacia())):
	
	
		while True:
			########################
	

			if wait:
				button , value = window.Read()	
		
			if button in (None , 'EXIT'):
				exit()		
			
			if button=='COMENZAR' and wait:
				###		
				inicio=time.time()
				"""
				bolsa.quitar_fichas("A",8)				
				window.FindElement("AA").update(bolsa.cant_letras("A"))
				if bolsa.bolsa_vacia():
					break
				"""

				#VARIABLES USADAS PARA MOSTRAR EL CRONOMETRO EN PANTALLA
				current_time = 0
				paused = False
				start_time = int(round(time.time() * 100))

				window.FindElement('PASAR').update(disabled=False)
				window.FindElement('GUARDAR').update(disabled=False)
				window.FindElement('CHECK').update(disabled=False)
				#window.FindElement('PASAR TURNO').update(disabled=False)
				window.FindElement('COMENZAR').update(disabled=True)
				window['COMENZAR'].update( button_color=('white','red'))
				wait=False
				opc2=random.randint(0,1)
				if opc2==1:
					print('empieza el jugador')

				
						
			if not(wait):
			
	
				if (opc2==0)and wait2:
					PC.inteligencia(controlAt,window,boardConfig,images,listadoPc,clasificar,images_keys,conf,fichasIA)
					print('IA INICIAL')
					wait2=False
				while True:
					current_time = int(round(time.time() * 100)) - start_time
					# minu = current_time // 100 // 60
					# seg = current_time // 100 % 60
					# mil = current_time % 100
					window['reloj'].update('{:02d}:{:02d}.{:02d}'.format((current_time // 100) // 60,
                                                                  (current_time // 100) % 60,
                                                                  current_time % 100),background_color=('red'))
					if conf.getConfiguracionesSeleccionadas()['tiempo'] == 'minimo':
						if (current_time // 100) // 60 == 5:
							print('=============================================5 MINUTOS====================================')
							print('=============================================5 MINUTOS====================================')
							print('=============================================5 MINUTOS====================================')
							print('=============================================5 MINUTOS====================================')
							sg.Popup('SE ACABO EL TIEMPO!!!')
							window.close()
					
					if conf.getConfiguracionesSeleccionadas()['tiempo'] == 'medio':
						if (current_time // 100) // 60 == 15:
							print('=============================================15 MINUTOS====================================')
							print('=============================================15 MINUTOS====================================')
							print('=============================================15 MINUTOS====================================')
							print('=============================================15 MINUTOS====================================')
							sg.Popup('SE ACABO EL TIEMPO!!!')
							window.close()

					if conf.getConfiguracionesSeleccionadas()['tiempo'] == 'maximo':
						if (current_time // 100) // 60 == 30:
							print('=============================================30 MINUTOS====================================')
							print('=============================================30 MINUTOS====================================')
							print('=============================================30 MINUTOS====================================')
							print('=============================================30 MINUTOS====================================')
							sg.Popup('SE ACABO EL TIEMPO!!!')
							window.close()

					puntosP=0
					puntosL=0
					#letra=''
					l=-1
					button , value = window.Read(timeout=10)
					#type(button) is tuple
					
					# if button == 'PASAR TURNO':
						# wait2=True
						# break
					if button == 'CHECK':
						p = ""
						p = p.join(palabra)
						j
						if palabra == '':
							sg.Popup('todavia no formo una palabra')
						elif len(palabra[0])>1:
							if (clasificar.comprobarPalabraEnBaseAlNivel(palabra[0], conf)):
								
								
								#print(palabra[0])
								sg.Popup('PALABRA FORMADA : ' ,palabra)
								print(clasificar.comprobarPalabraEnBaseAlNivel(palabra[0], conf))

								#palabra[0]=''
								T2= True
								T1=True
								T3= True
								F=0
								C=0
								#cant=cant+1
								#x=0
								T4=True
								
								if (clasificar.comprobarPalabraEnBaseAlNivel(palabra[0], conf)):
									
									palabra[0]=''
									actualizarAtrilJugador()
									wait2=True
								listadoPosicionLetrasAtril=[]
								listadoPosicionLetrasTablero=[]
								### se agrega el puntaje a la lista
								listado.append(p + " " + str(bolsa.calcular_puntos(p,word_values)) + " Puntos")
								actualizar_listado(window.FindElement('datosj'))
								puntaje_jugador = puntaje_jugador + bolsa.calcular_puntos(p,word_values) 
								print(puntaje_jugador)
								#####
							else:
								sg.Popup('PALABRA INVALIDA')
								
								devolverLetras()
								T2=True
								T3=True
								T1=True
								T4=True
								palabra[0]=''
								listadoPosicionLetrasAtril=[]
								listadoPosicionLetrasTablero=[]								
							##window[]
						# if len(word)>= 2 and len(word) <=7:
						elif len(palabra[0])<2:
							sg.Popup('la palabra es menor de 2')
							#break
						del word_values[:]
						
													
										
					if button in (None , 'EXIT'):
						exit()
			
												
					if button =='PASAR':
						cantPasadas=cantPasadas+1
						controlAt=[7,7,0,0]
						# if cantPasadas==3:
							# window.FindElement('PASAR').update(disabled=True)
						
						if cantPasadas<4:
							
							initial_atril=PasarTurno(initial_atril)
							listadoPosicionLetrasAtril=[]
							listadoPosicionLetrasTablero=[]
							palabra=['']
							T1=True
							T2=True
							#T3=True
							T4=True
							
							listado=[]
							listadoPosicionLetrasAtril=[]
							listadoPosicionLetrasTablero=[]									
							
						
							PC.inteligencia(controlAt,window,boardConfig,images,listadoPc,clasificar,images_keys,conf,fichasIA)
														
						else:
							sg.Popup('se supero la cantidad de pasadas')

						
							
					if type(button) is int:
						print(button)
					
						if initial_atril[button] !='':
							i=button
							letra= initial_atril[button]
							#####hoy palabra += letra
							button , value = window.Read()
							while(type(button)is not(tuple)):
								button , value = window.Read()			
							#button , value = window.Read()
							if type(button) is tuple:
								
								if not(boardConfig[7][7].get_estado()):
									print('posicion central no  ocupada')
														
								
								if not(boardConfig[7][7].get_estado()):
									print('posicion central no  ocupada')
														
								
									if (button[0]==7 and button[1]==7)and T3 :
										print(button)
										modificarBoton(word_values)
										T3=False
										F=button[0]
										C=button[1]
										cant=0
									#print(type(lista[1]))
									if not(T3):
										if(button[0]==F)and T1:
											if C<button[1]and(button[1]==C+1):
												T2=False
												modificarBoton(word_values)
												C=button[1]
										if(button[1]==C)and T2:
											if F<button[0]and(button[0]==F+1):
												print(button)
												T1=False
												modificarBoton(word_values)
												F=button[0]
									#cant=4
									
										
																			
								else:
																
								#if cant<10: ## la cantidad de palabras formadas con 7 letras
				
									if T4:										
										
																
										
										modificarBoton(word_values)
										F=button[0]
										C=button[1]
										T4=False
									else:
										if(button[0]==F)and T1 :
											if C<button[1]and(button[1]==C+1):
												T2=False
												modificarBoton(word_values)
												C=button[1]
										if(button[1]==C)and T2:
											if F<button[0]and(button[0]==F+1):
												T1=False
												modificarBoton(word_values)
												F=button[0]				
											
							
								
								actualizar_listado(window.FindElement('datosj')) ## habria que multiplicar el valor de cada letra o palabra
								print("ESTE ES EL PUNTAJE DEL JUGADOR: -------------" + str(puntaje_jugador))
								## modifiquenlo para que muestres los puntos que se van acumulando por casillas 
								##
																			
																			
								l=0
					
					
				if type(button) is tuple:
					if l ==-1:
						
						sg.Popup('movimiento incorrecto')
			
				if (opc2==1)and wait2:
					PC.inteligencia(controlAt,window,boardConfig,images,listadoPc,clasificar,images_keys, conf,fichasIA)
					print('IA FINAL')
					controlAt=[8,7,0,0]
			"""control del fin del tiempo de juego."""						
			final=time.time()
			if final-inicio>120:			
				break
			try:
				if (current_time // 100) % 60 == 10:
					print('=============================================10 SEGUNDOS====================================')
					print('=============================================10 SEGUNDOS====================================')
					print('=============================================10 SEGUNDOS====================================')
					print('=============================================10 SEGUNDOS====================================')
			except:
				print('porfavor, aprete el boton comenzar')
		sg.Popup('FIN Juego')
		wait=True
		window.FindElement('PASAR').update(disabled=True)
		window.FindElement('GUARDAR').update(disabled=True)
		window.FindElement('CHECK').update(disabled=True)
		#window.FindElement('PASAR TURNO').update(disabled=True)		
		
		window.FindElement('COMENZAR').update(disabled=False)
		window['COMENZAR'].update( button_color=('white','green'))	
		while(button!='COMENZAR'):
			button , value = window.Read()
	
		if button=='COMENZAR':
			initial_atril=[]
			images_keys= list(images.keys()) ### seria la lista de palabras
			print(images_keys)
			images_keys.remove('BLANK')
			random.shuffle(images_keys,random.random)
			initial_atril=[]
			initial_atril2=[]
			PC.atrilPalabrasValidas(images_keys,initial_atril2, conf)
			initial_atril=initial_atril2[:]			
			
			
	
			for i in range(7):
				#window[i].update(initial_atril[i])
				piece_image = images[initial_atril[i]]
								
				img=piece_image['imagen']

				window[i].update(image_filename=img,image_size=(50, 50), button_color=('',''))
	##### blanquear tablero
	
	
			#actulizarTablero(opc)
			BorrarTablerGeneral()#cant=4
			T1=True
			T2=True
			T3=True
			palabra=['']
			listado=[]
			listadoPc=[]
			listadoPosicionLetrasAtril=[]
			listadoPosicionLetrasTablero=[]
			initial_atril2=[]			
			cantPasadas=0
			actualizar_listado(window.FindElement('datosj'))
			actualizar_listado(window.FindElement('datosm'))
			controlAt=[7,7,0,0]	
			#window['COMENZAR'].update( button_color=('white','green'))		
			bolsa = Bolsa(conf.getConfiguracionLetras())
			
						
					
if __name__ == "__main__":

    main_game(1)

