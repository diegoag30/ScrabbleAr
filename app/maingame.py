import PySimpleGUI as sg
import random
from itertools import combinations
import time
import clasificarPalabra
import IA
import os.path
import config_tablero
from Bolsa import Bolsa
base_path=os.path.dirname(os.path.abspath(__file__))
##anda genial
def main_game(num_tablero):
	
	#Bolsa instanciada, 
	bolsa = Bolsa(50)
	PC=IA
	clasificar=clasificarPalabra


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
	images_keys= list(images.keys()) ### seria la lista de palabras
	images_keys.remove('BLANK')
	random.shuffle(images_keys,random.random)
	initial_atril=[]
	initial_atril2=[]
	PC.atrilPalabrasValidas(images_keys,initial_atril2)
	initial_atril=initial_atril2[:]
	



	# for i in range(0,7):
		# initial_atril.append(random.choice(images_keys))	
	#########################################################
	# atril2=''
	# listaPalabras=[]
	# cont3=3
	
	# for c in combinations(images_keys,cont3):
		# lp="".join(c)
		# #print(lp)
		# listaPalabras.append(lp)
	
	# cont=len(listaPalabras)
	# cont2=0
	# while (cont!=cont2) and True:
		
		# if clasificar.comprobarPalabraEnBaseAlNivel(listaPalabras[cont2]):
			# print(listaPalabras[cont2])
			# print('*'*30)
			# atril2=atril2+listaPalabras[cont2][0]
			# atril2=atril2+listaPalabras[cont2][1]
			# atril2=atril2+listaPalabras[cont2][2]
		
		
	
			# #T=False
			# #IA(listaPalabras[cont2])
			# if len(atril2)==6:
				# atril2=atril2+(random.choice(images_keys))
				# break
		
				
				
			# #T=False
		# cont2=cont2+1
		
		
		# if cont==cont2:
			
			# break
	# if len(atril2)<7:
		# while True:
			# atril2=atril2+(random.choice(images_keys))
			# if len(atril2)==7:
				# break

	# for i in atril2:
		# initial_atril.append(i)			
	# # for i in range(0,7):
		# initial_atril.append(random.choice(images_keys))								
#########################
	class Tablero():
		
	
 		#sg.RButton(texto,image_size=(50, 50), pad=(2,2),key=key)

	
		def render_square(self, image ,key , texto= '',color_button=('white','white')):
		#return sg.RButton(texto,image_filename=image,image_size=(50, 50), pad=(2,2),key=key,button_color=color_button) 
		
			return sg.RButton(texto,image_filename=image,image_size=(50, 50), pad=(2,2),key=key,button_color=color_button)		



			
			
			
	class Tablero1(Tablero):
		def Tab(self,images):
	
	
			tamaño=(50,50)
		
	
		
				
				
			tablero1=[]
			for i in range(15):
				row=[]
				for j in range(15):
					piece_image = images['BLANK']
					valor=boardConfig[i][j].get_valor()
					color=boardConfig[i][j].get_color()
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
			
			
			
	class Tablero2(Tablero):
		def Tab(self,images):
	
	
			tamaño=(50,50)
		
	
		
				
				
			tablero1=[]
			for i in range(15):
				row=[]
				for j in range(15):
					piece_image = os.path.join(base_path,'images/fond2.png')
					valor=boardConfig[i][j].get_valor()
					color=boardConfig[i][j].get_color()
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
						#piece_image=os.path.join(base_path,'images/PX-3Cr.png')
						
						row.append(self.render_square(piece_image,key =(i,j),texto='', color_button=('white','red')))
					elif color == 'blue':
						#piece_image=os.path.join(base_path,'images/PX2.png')
						piece_image = images_PuntosNv1['LX3']
						row.append(self.render_square(piece_image,key =(i,j),texto='', color_button=('white','blue')))
					elif color == 'violet':
						piece_image=os.path.join(base_path,'images/centro.png')
						row.append(self.render_square(piece_image,key =(i,j),texto='', color_button=('white','Dark violet')))												
					elif color == 'orange':
						piece_image=os.path.join(base_path,'images/PX-2.png')
						#piece_image = images_PuntosNv1['PX2']
						#piece_image=os.path.join(base_path,'images/LX-3Cr.png')
						row.append(self.render_square(piece_image,key =(i,j),texto='', color_button=('white','orange')))




						
					else:
						color_button=('white','white')
						piece_image = os.path.join(base_path,'images/fond2.png')
						row.append(self.render_square(piece_image,key =(i,j),texto=''))
		
				tablero1.append(row)
		
			return (tablero1,tamaño)			
			
			
	class Tablero3(Tablero):
		def Tab(self,images):
	
	
			tamaño=(50,50)
		
	
		
				
				
			tablero1=[]
			for i in range(15):
				row=[]
				for j in range(15):
					piece_image = os.path.join(base_path,'images/fond2.png')
					valor=boardConfig[i][j].get_valor()
					color=boardConfig[i][j].get_color()
					# if color == 'violet':
						# piece_image=os.path.join(base_path,'images/corona.png')
						# row.append(render_square(piece_image,key =(i,j),texto='', color_button=('white','Dark violet')))
						

					# elif valor == 2:
						# piece_image=os.path.join(base_path,'images/P2.png')
						# row.append(render_square(piece_image,key =(i,j),texto='', color_button=('white','orange')))
					if color == 'green':
						piece_image=os.path.join(base_path,'images/LX-2Cr.png')
						#piece_image = images_PuntosNv1['LX2']
						row.append(self.render_square(piece_image,key =(i,j),texto='', color_button=('white','green')))
			
					elif color == 'red':
						#piece_image=os.path.join(base_path,'images/P2.png')
						#piece_image = images_PuntosNv1['PX3']
						piece_image=os.path.join(base_path,'images/PX3ESC.png')
						
						row.append(self.render_square(piece_image,key =(i,j),texto='', color_button=('white','red')))
					elif color == 'blue':
						piece_image=os.path.join(base_path,'images/LX-3Cr.png')
						#piece_image = images_PuntosNv1['LX3']
						row.append(self.render_square(piece_image,key =(i,j),texto='', color_button=('white','blue')))
					elif color == 'violet':
						piece_image=os.path.join(base_path,'images/corona1.png')
						row.append(self.render_square(piece_image,key =(i,j),texto='', color_button=('white','Dark violet')))												
					elif color == 'orange':
						piece_image=os.path.join(base_path,'images/PX2ESC.png')
						#piece_image = images_PuntosNv1['PX2']
						row.append(self.render_square(piece_image,key =(i,j),texto='', color_button=('white','orange')))




						
					else:
						color_button=('white','white')
						piece_image = os.path.join(base_path,'images/fond3.png')
						row.append(self.render_square(piece_image,key =(i,j),texto=''))
		
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
			''' modificartBoton () cambia el estado del boton , cambia la imagen de una pieza del tablero y consta que esta ocupado'''
	def modificarBoton(): 
		#if boardConfig[button[0]][button[1]].get_estado() == True:
			#print('')
	
		if boardConfig[button[0]][button[1]].get_estado() == False:
			img=''
			window[i].update(image_filename=img,image_size=(50, 50), button_color=('',''))
			
			
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
	
			if boardConfig[button[0]][button[1]].get_tipo() =='L':
				
				#puntosL=boardConfig1[button[0]][button[1]].get_valor()
				#puntosl='puntos PxP'+str(puntosL)
				listado.append('LetraX'+str(boardConfig[button[0]][button[1]].get_valor()))
				### crear una lista que para los puntos por letra que despues los multiplicamos lor el valor de las letra
				
			
			elif boardConfig[button[0]][button[1]].get_tipo() =='P':
				#puntosP=boardConfig1[button[0]][button[1]].get_valor()
				listado.append('PalabraX'+str(boardConfig[button[0]][button[1]].get_valor()))
				
				### crear una lista que para los puntos por palabra que despues los multiplicamos lor el valor de letra
			
		


	# def devolverLetras():
		# p=palabra[0]
		# print(p)
		# cont=0
		# for i in listadoPosicionLetrasAtril:
			# piece_image = images[p[cont]]
			# img=piece_image['imagen']
			# window[i].update(image_filename=img,image_size=(50, 50), button_color=('',''))
			# piece_image = images['BLANK']
			# img=piece_image['imagen']
			# boardConfig[listadoPosicionLetrasTablero[cont][0]][listadoPosicionLetrasTablero[cont][1]].set_estado(False)
			# #color=boardConfig[listadoPosicionLetrasTablero[cont][0][listadoPosicionLetrasTablero[cont][1]].get_color()
			# color=boardConfig[listadoPosicionLetrasTablero[cont][0]][listadoPosicionLetrasTablero[cont][1]].get_color()
			# if color == 'violet':
				# piece_image=os.path.join(base_path,'images/centro.png')
				# window[listadoPosicionLetrasTablero[cont]].update(image_filename=piece_image, image_size= tamaño_img ,button_color=('white','white'))
			# else:
				# window[listadoPosicionLetrasTablero[cont]].update(image_filename=img, image_size= tamaño_img ,button_color=('white','white'))
			# cont=cont+1

	def devolverLetras():
		p=palabra[0]
		print(p)
		cont=0
		for i in listadoPosicionLetrasAtril:
			piece_image = images[p[cont]]
			img=piece_image['imagen']
			window[i].update(image_filename=img,image_size=(50, 50), button_color=('',''))
			initial_atril[i]=p[cont]
			piece_image = images['BLANK']
			img=piece_image['imagen']
			boardConfig[listadoPosicionLetrasTablero[cont][0]][listadoPosicionLetrasTablero[cont][1]].set_estado(False)
			#color=boardConfig[listadoPosicionLetrasTablero[cont][0][listadoPosicionLetrasTablero[cont][1]].get_color()
			color=boardConfig[listadoPosicionLetrasTablero[cont][0]][listadoPosicionLetrasTablero[cont][1]].get_color()
			if color == 'violet':
				piece_image=os.path.join(base_path,'images/corona.png')
				window[listadoPosicionLetrasTablero[cont]].update(image_filename=piece_image, image_size= tamaño_img ,button_color=('white','white'))
			else:
				window[listadoPosicionLetrasTablero[cont]].update(image_filename=img, image_size= tamaño_img ,button_color=('white','white'))
			cont=cont+1

		print(initial_atril)					

	def actualizarAtrilJugador():
		initial_atril2=[]
		random.shuffle(images_keys,random.random)
		PC.atrilPalabrasValidas(images_keys,initial_atril2)
			
		for i in range(0,7):
			if initial_atril[i]=='':
				# initial_atril[i]=random.choice(initial_atril2)
				initial_atril[i]=initial_atril2[i]
				piece_image = images[initial_atril[i]]
				img=piece_image['imagen']
				window[i].update(image_filename=img,image_size=(50, 50), button_color=('',''))
		print(initial_atril)
							










			
	def actualizar_listado(listbox):
		

		listbox.Update(listado)	## accedo a la tupla			

	def actulizarTablero (opc):
		def BorrarTablero1(color):
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
			   
			   
		def BorrarTablero2(color):
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
			    piece_image=os.path.join(base_path,'images/centro.png')
			#row.append(self.render_square(piece_image,key =(i,j),texto='', color_button=('white','white')))
			    window[(i,j)].update(image_filename=piece_image, image_size= tamaño_img ,button_color=('white','Dark violet'))												
			elif color == 'orange':
			    #piece_image = images_PuntosNv1['PX2']
			    piece_image=os.path.join(base_path,'images/PX-2.png')
			#row.append(self.render_square(piece_image,key =(i,j),texto='', color_button=('white','orange')))
			    window[(i,j)].update(image_filename=piece_image, image_size= tamaño_img ,button_color=('white','orange'))
						
			else:
			#color_button=('white','white')
			   # piece_image = images['BLANK']
			   # piece_image = piece_image['imagen']
			   piece_image=os.path.join(base_path,'images/fond2.png')
			#row.append(self.render_square(piece_image['imagen'],key =(i,j),texto='')) 
			   window[(i,j)].update(image_filename=piece_image, image_size= tamaño_img ,button_color=('white','white'))			   
			   
			   
			   
			   
		def BorrarTablero3(color):
			if color == 'green':
				piece_image = images_PuntosNv1['LX2']
				piece_image=os.path.join(base_path,'images/LX-2Cr.png')
				#row.append(self.render_square(piece_image,key =(i,j),texto='', color_button=('white','green')))
				window[(i,j)].update(image_filename=piece_image, image_size= tamaño_img ,button_color=('white','green'))
		
			elif color == 'red':
				
				piece_image=os.path.join(base_path,'images/PX3ESC.png')
			#row.append(self.render_square(piece_image,key =(i,j),texto='', color_button=('white','red')))
			

				window[(i,j)].update(image_filename=piece_image, image_size= tamaño_img ,button_color=('white','red'))
			elif color == 'blue':
			    piece_image = images_PuntosNv1['LX3']
			    piece_image=os.path.join(base_path,'images/LX-3Cr.png')
			#row.append(self.render_square(piece_image,key =(i,j),texto='', color_button=('white','blue')))
			    window[(i,j)].update(image_filename=piece_image, image_size= tamaño_img ,button_color=('white','blue'))
			elif color == 'violet':
			    piece_image=os.path.join(base_path,'images/corona1.png')
			#row.append(self.render_square(piece_image,key =(i,j),texto='', color_button=('white','white')))
			    window[(i,j)].update(image_filename=piece_image, image_size= tamaño_img ,button_color=('white','Dark violet'))												
			elif color == 'orange':
			    #piece_image = images_PuntosNv1['PX2']
			    piece_image=os.path.join(base_path,'images/PX2ESC.png')
			#row.append(self.render_square(piece_image,key =(i,j),texto='', color_button=('white','orange')))
			    window[(i,j)].update(image_filename=piece_image, image_size= tamaño_img ,button_color=('white','orange'))
						
			else:
			#color_button=('white','white')
			
			   piece_image=os.path.join(base_path,'images/fond3.png')
			#row.append(self.render_square(piece_image['imagen'],key =(i,j),texto='')) 
			   window[(i,j)].update(image_filename=piece_image, image_size= tamaño_img ,button_color=('white','white'))			   
			   
			   
			   
			   
			   
			   
			   
			   
			   
			   
			   
		if opc ==1:
			
			for i in range(15):
				for j in range(15):
					window[(i,j)].update('')
					boardConfig[i][j].set_estado(False)
					color=boardConfig[i][j].get_color()
					BorrarTablero1(color)	
						  
		if opc ==2:
			
			for i in range(15):
				for j in range(15):
					window[(i,j)].update('')
					boardConfig[i][j].set_estado(False)
					color=boardConfig[i][j].get_color()
					BorrarTablero2(color)				
			
		if opc ==3:
			
			for i in range(15):
				for j in range(15):
					window[(i,j)].update('')
					boardConfig[i][j].set_estado(False)
					color=boardConfig[i][j].get_color()
					BorrarTablero3(color)				
		
		
		
		
		
		
		
		
		
						# for i in range(15):
					# for j in range(15):
						# window[(i,j)].update('')
						# boardConfig[i][j].set_estado(False)
						# color=boardConfig[i][j].get_color()
						# BorrarTablero1(color)			
			
			
####################
	#inteligencia1.saludo()
	atr1=atril1(True).crearAtril()
	atr2=atril1(False).crearAtril()
	if num_tablero ==1:
		obj = Tablero1()
		opc=1
	elif num_tablero == 2:
		obj = Tablero2()	
		opc=2	
	elif num_tablero ==3:
		obj = Tablero3()
		opc=3
	#bolsa.sacar_fichas(14)		

	#opc=1 # 2 para borrar el tablero 2 , 3 para el tablero 3 se tiene que elegir cuando se elige el tablero
	print('*')
	boardConfig=config_tablero.Config1() ## para enganchar con el menu existen 3 configuraciones
	#boardConfig=config_tablero.Config2() casillas naranjas descuentan puntos por palabra x-2
	##boardConfig=config_tablero.Config3 () verde y azul quitan puntos

	elementos=obj.Tab(images) ##### estaria para conectarlo con una opcion para elegir el tablero
	tablero= elementos[0] 
	tamaño_img = elementos[1]

	columna_2 = [ [sg.Text('PUNTOS MAQUINA')],[sg.Listbox(values =[], key='datosm', font='Courier 18' ,size=(20,10))],[sg.Text('TOTAL PUNTOS')],[sg.Text('FICHAS RESTANTES', size=(20, 2), justification='center')],[sg.Text(str(bolsa.get_fichas_restantes()) , size=(20, 2), justification='center',key='bolsa_fichas')],]
	columna_1 = [ [sg.Text('PUNTOS JUGADOR')],[sg.Listbox(values =[], key='datosj', font='Courier 18',size=(20,10))],[sg.Text('TOTAL PUNTOS')]]
	columna_3 = [ [sg.Text('Total Puntos')]]				
	


	board_tab=[[sg.Button('CHECK',disabled=True)],[sg.Column(columna_1),sg.Column(atr1),sg.Column(tablero),sg.Column(atr2),sg.Column(columna_2)],[sg.Button('COMENZAR',button_color=('white','green')),sg.Button('PASAR',disabled=True),sg.Button('GUARDAR',disabled=True),sg.Button('PASAR TURNO',disabled=True),sg.Button('EXIT')]]
	window = sg.Window('ScrabbleAr',default_button_element_size=(12,1), auto_size_buttons=False).Layout(board_tab)
	cantPasadas=0
	#palabra=''	
	controlAt=[7,7,0,0]

	palabra=['']
	#i=0
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
	listadoPosicionLetrasAtril=[]
	listadoPosicionLetrasTablero=[]
	listadoPc=[]
	listado=[]
	#inicio=time.time()
	wait=True
	wait2=True
	window.Finalize()
	inicio=time.time()
	iniciar=True
	
	while True and iniciar:
		# random.shuffle(images_keys,random.random)
		# PC.atrilPalabrasValidas(images_keys,initial_atril2)
		# initial_atril=initial_atril2[:]		
	
		while True :
			########################
			if wait:
				button , value = window.Read()	
		
			if button in (None , 'EXIT'):
				exit()		
			
			if button=='COMENZAR' and wait:
				#Actualizacion bolsa
				bolsa.sacar_fichas(14)
				window.FindElement('bolsa_fichas').update(str(bolsa.get_fichas_restantes()))
				###		
				inicio=time.time()
				window.FindElement('PASAR').update(disabled=False)
				window.FindElement('GUARDAR').update(disabled=False)
				window.FindElement('CHECK').update(disabled=False)
				window.FindElement('PASAR TURNO').update(disabled=False)
				window.FindElement('COMENZAR').update(disabled=True)
				window['COMENZAR'].update( button_color=('white','red'))
				wait=False
				opc2=random.randint(0,1)
				if opc2==1:
					print('empieza el jugador')			
				
						
			if not(wait):
			
				# window.FindElement('PASAR').update(disabled=False)
				# window.FindElement('GUARDAR').update(disabled=False)
				# window.FindElement('CHECK').update(disabled=False)
				# window.FindElement('PASAR TURNO').update(disabled=False)
				# window.FindElement('COMENZAR').update(disabled=True)				
						
			#########################
				if (opc2==0)and wait2:
					PC.inteligencia(controlAt,window,boardConfig,images,listadoPc,clasificar,images_keys)
					print('IA INICIAL')
					wait2=False
				while True:
					puntosP=0
					puntosL=0
					#letra=''
					l=-1
					button , value = window.Read()
					#type(button) is tuple
					
					if button == 'PASAR TURNO':
						wait2=True
						break
					if button == 'CHECK':
						j
						if palabra == '':
							sg.Popup('todavia no formo una palabra')
						elif len(palabra[0])>1:
							if (clasificar.comprobarPalabraEnBaseAlNivel(palabra[0])):
								
								
								print(palabra[0])
								sg.Popup('PALABRA FORMADA : ' ,palabra)
								print(clasificar.comprobarPalabraEnBaseAlNivel(palabra[0]))
								#palabra[0]=''
								T2= True
								T1=True
								T3= True
								F=0
								C=0
								#cant=cant+1
								#x=0
								T4=True
								
								if (clasificar.comprobarPalabraEnBaseAlNivel(palabra[0])):
									
									palabra[0]=''
									actualizarAtrilJugador()
									wait2=True
								listadoPosicionLetrasAtril=[]
								listadoPosicionLetrasTablero=[]								
								break
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


										
					if button in (None , 'EXIT'):
						exit()
			
						
						
						
					if button =='PASAR':
						cantPasadas=cantPasadas+1
						if cantPasadas<4:
					
							initial_atril=[]
							for i in range(0,7): ##cambiar i
								initial_atril.append(random.choice(images_keys))
							for i in range(7):
								#window[i].update(initial_atril[i])
								piece_image = images[initial_atril[i]]
												
								img=piece_image['imagen']
			
								window[i].update(image_filename=img,image_size=(50, 50), button_color=('',''))
					##### blanquear tablero
					
					
							actulizarTablero(opc)
							listadoPosicionLetrasAtril=[]
							listadoPosicionLetrasTablero=[]
							# for i in range(15):
								# for j in range(15):
									# window[(i,j)].update('')
									# boardConfig[i][j].set_estado(False)
									# color=boardConfig[i][j].get_color()
									# BorrarTablero1(color)
							#Actualizacion bolsa
							bolsa.sacar_fichas(7)
							window.FindElement('bolsa_fichas').update(str(bolsa.get_fichas_restantes()))
							###	
							PC.inteligencia(controlAt,window,boardConfig,images,listadoPc,clasificar,images_keys)							
						else:
							sg.Popup('se supero la cantidad de pasadas')
						cant=4
						T1=True
						T2=True
						T3=True
						palabra=['']
						listado=[]
						listadoPosicionLetrasAtril=[]
						listadoPosicionLetrasTablero=[]						
						actualizar_listado(window.FindElement('datosj'))
			
						
							
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
														
								
									if (button[0]==7 and button[1]==7)and T3 :
										print(button)
										modificarBoton()
										T3=False
										F=button[0]
										C=button[1]
										cant=0
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
									#cant=4	
								else:
																
								#if cant<10: ## la cantidad de palabras formadas con 7 letras
				
									if T4:
										#x=x+1
										modificarBoton()
										F=button[0]
										C=button[1]
										T4=False
									else:
										if(button[0]==F)and T1:
											if C<button[1]:
												T2=False
												modificarBoton()
												C=button[1]
										if(button[1]==C)and T2:
											if F<button[0]:
												T1=False
												modificarBoton()
												F=button[0]				
											
								## puntos mostrar por letra o palabra solo voy a mostar los puntos por las casillas
								
								actualizar_listado(window.FindElement('datosj')) ## habria que multiplicar el valor de cada letra o palabra
			
								## modifiquenlo para que muestres los puntos que se van acumulando por casillas 
								##
																			
								l=0
			
		
					
					
				if type(button) is tuple:
					if l ==-1:
						
						sg.Popup('movimiento incorrecto')
			
				if (opc2==1)and wait2:
					PC.inteligencia(controlAt,window,boardConfig,images,listadoPc,clasificar,images_keys)
					print('IA FINAL')
					controlAt=[8,7,0,0]
			final=time.time()
			if final-inicio>120:
			
				break		
		sg.Popup('FIN Juego')
		wait=True
		window.FindElement('PASAR').update(disabled=True)
		window.FindElement('GUARDAR').update(disabled=True)
		window.FindElement('CHECK').update(disabled=True)
		window.FindElement('PASAR TURNO').update(disabled=True)		
		
		window.FindElement('COMENZAR').update(disabled=False)
		window['COMENZAR'].update( button_color=('white','green'))	
		while(button!='COMENZAR'):
			button , value = window.Read()
	
		if button=='COMENZAR':
			initial_atril=[]
			images_keys= list(images.keys()) ### seria la lista de palabras
			images_keys.remove('BLANK')
			random.shuffle(images_keys,random.random)
			initial_atril=[]
			initial_atril2=[]
			PC.atrilPalabrasValidas(images_keys,initial_atril2)
			initial_atril=initial_atril2[:]			
			
			
			# initial_atril=[]
			# for i in range(0,7): ##cambiar i
				# initial_atril.append(random.choice(images_keys))
			for i in range(7):
				#window[i].update(initial_atril[i])
				piece_image = images[initial_atril[i]]
								
				img=piece_image['imagen']

				window[i].update(image_filename=img,image_size=(50, 50), button_color=('',''))
	##### blanquear tablero
	
	
			actulizarTablero(opc)
						#cant=4
			T1=True
			T2=True
			T3=True
			palabra=['']
			listado=[]
			listadoPc=[]
			listadoPosicionLetrasAtril=[]
			listadoPosicionLetrasTablero=[]
			initial_atril2=[]			
			
			actualizar_listado(window.FindElement('datosj'))
			actualizar_listado(window.FindElement('datosm'))
			controlAt=[7,7,0,0]	
			#window['COMENZAR'].update( button_color=('white','green'))		
			
			
						
					
if __name__ == "__main__":

    main_game(1)			


