import PySimpleGUI as sg
import time
import random
import os.path
import config_tablero
import clasificarPalabra
from Bolsa import Bolsa
from itertools import combinations
import random
from pattern.es import verbs, tag, spelling, lexicon
import string
from pattern.es import singularize , pluralize, conjugate , INFINITIVE , PRESENT , PAST , SG , PERFECTIVE , SUBJUNCTIVE ,PL ,parse
base_path=os.path.dirname(os.path.abspath(__file__))

def main_game(num_tablero):
	
	#Bolsa instanciada, 
	bolsa = Bolsa(50)
	###
	chequearPalabra=clasificarPalabra
	controlAt=[0,0,0,0]	


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
#########



	

	def inteligenia():
			
		def IA(initial_atril2):
	            # piece_image = images[initial_atril[i]]
				# img=piece_image['imagen']
				# window[button].update(image_filename=img, image_size= tamaño_img ,button_color=('white','grey'))		
			
			tamaño_img=(50,50)
			def horizontal():
				T=True;
				while T and controlAt[0]<15 :
					if controlAt[1]+len(initial_atril2)-1<=14: ## 
						L=True
						cont=0
						print(controlAt,':',boardConfig[controlAt[0]][controlAt[1]+cont].get_estado())
						while L and (cont<len(initial_atril2)):
							if boardConfig[controlAt[0]][controlAt[1]+cont].get_estado() == True:
								L=False
								
								print(controlAt)
								print(boardConfig[controlAt[0]][controlAt[1]].get_estado())
							#T=False
							else:
								cont=cont+1 
						cont=0
						if L:
							for i in range (len(initial_atril2)): 
								controlAt[1]=controlAt[1]+cont
								cont=1
								B=(controlAt[0],controlAt[1])
								piece_image=images[initial_atril2[i]]
								img=piece_image['imagen']
								window[B].update(image_filename=img, image_size= tamaño_img ,button_color=('white','red'))
								#window[B].update(initial_atril2[i])
								boardConfig[controlAt[0]][controlAt[1]].set_estado(True) 
		
							if controlAt[1]==14:
								controlAt[1]=0
								controlAt[0]=controlAt[0]+1
							else:
								controlAt[1]=controlAt[1]+1##
							T=False
						else:
							 ### trato de escribir en vertical
							print(controlAt)
							if controlAt[0]+len(initial_atril2)-1<=14:
								L=True
								cont=0
								while L and (cont<len(initial_atril2)):##
									if boardConfig[controlAt[0]+cont][controlAt[1]].get_estado() == True:
										L=False
										
									else:
										cont=cont+1
								cont=0
								if L:
									x=controlAt[0]
									for i in range(len(initial_atril2)):
										x=x+cont
										cont=1
										B=(x,controlAt[1])
										piece_image=images[initial_atril2[i]]
										img=piece_image['imagen']
										window[B].update(image_filename=img, image_size= tamaño_img ,button_color=('white','red'))									
										
										#window[B].update(initial_atril2[i])
										boardConfig[x][controlAt[1]].set_estado(True)
									if controlAt[1]==14:
										controlAt[1]=0
										controlAt[0]=controlAt[0]+1
									else:
										controlAt[1]=controlAt[1]+1 #aqui
									T=False#lllllllllll
								else:###zzzz
							
									if controlAt[1]==14:
										controlAt[1]=0
										controlAt[0]=controlAt[0]+1
									else:
										controlAt[1]=controlAt[1]+1 ##aquillllllllll	
							else:###
								print('final')
								if controlAt[1]==14:
									controlAt[1]=0
									controlAt[0]=controlAt[0]+1
								else:
									controlAt[1]=controlAt[1]+1 #aquillllzzz
								
									
					else:
						 ### voy a cambiar la orientacion a vertical
						if controlAt[0]+len(initial_atril2)-1<=14:
							L=True
							cont=0 
							while L and(cont<len(initial_atril2)):
								if boardConfig[controlAt[0]+cont][controlAt[1]].get_estado() == True:
									L=False
									print('lugar ocupado ',controlAt)
								else:
									cont=cont+1 
							
							cont=0
							if L:
								x=controlAt[0]
								for i in range(len(initial_atril2)):
									x=x+cont
									cont=1
									B=(x,controlAt[1])
									piece_image=images[initial_atril2[i]]
									img=piece_image['imagen']
									window[B].update(image_filename=img, image_size= tamaño_img ,button_color=('white','red'))								
									
									#window[B].update(initial_atril2[i])
									boardConfig[x][controlAt[1]].set_estado(True) 
								if controlAt[1]==14:
									controlAt[1]=0
									controlAt[0]=controlAt[0]+1
								else:
									controlAt[1]=controlAt[1]+1 
								T=False#
							else: ### 
								print('FF0')					
								if controlAt[1]==14:
									controlAt[1]=0
									controlAt[0]=controlAt[0]+1
								else:
									controlAt[1]=controlAt[1]+1##aqui
						else:
							print('la palabra no entro con la orientacion vertical')
							if controlAt[1]==14:
								controlAt[1]=0
								controlAt[0]=controlAt[0]+1
							else:
								controlAt[1]=controlAt[1]+1
							print(controlAt)#
				if(controlAt[0]==15):
					print('final')
					print(controlAt)
										
		
			def vertical():
				T=True;
				while T and controlAt[1]<15  :
					if controlAt[0]+len(initial_atril2)-1<=14: ## 
						L=True
						cont=0
						print(controlAt,':',boardConfig[controlAt[0]][controlAt[1]+cont].get_estado())
						while L and (cont<len(initial_atril2)):
							if boardConfig[controlAt[0]+cont][controlAt[1]].get_estado() == True:
								L=False
								print('x1')
								print(controlAt)
								print(boardConfig[controlAt[0]][controlAt[1]].get_estado())
							#T=False
							else:
								cont=cont+1 #
						cont=0
						if L:
							for i in range (len(initial_atril2)): 
								controlAt[0]=controlAt[0]+cont
								cont=1
								B=(controlAt[0],controlAt[1])
								piece_image=images[initial_atril2[i]]
								img=piece_image['imagen']
								window[B].update(image_filename=img, image_size= tamaño_img ,button_color=('white','red'))							
								#window[B].update(initial_atril2[i])
								boardConfig[controlAt[0]][controlAt[1]].set_estado(True) 
		
							if controlAt[0]==14:
								controlAt[0]=0
								controlAt[1]=controlAt[1]+1
							else:
								controlAt[0]=controlAt[0]+1## 
							T=False# 
						else:
							print('lugares ocupados0o')### ### trato de escribir en horizontal
							print(controlAt)
							if controlAt[1]+len(initial_atril2)-1<=14:
								L=True
								cont=0
								while L and (cont<len(initial_atril2)):##
									if boardConfig[controlAt[0]][controlAt[1]+cont].get_estado() == True:
										L=False
										print('lugar ocupadox2')
									else:
										cont=cont+1
								cont=0
								if L:
									y=controlAt[1]
									for i in range(len(initial_atril2)):
										y=y+cont
										cont=1
										B=(controlAt[0],y)
										piece_image=images[initial_atril2[i]]
										img=piece_image['imagen']
										window[B].update(image_filename=img, image_size= tamaño_img ,button_color=('white','red'))									
										#window[B].update(initial_atril2[i])
										boardConfig[controlAt[0]][y].set_estado(True)
									if controlAt[0]==14:
										controlAt[0]=0
										controlAt[1]=controlAt[1]+1
									else:
										controlAt[0]=controlAt[0]+1 #
									T=False#
								else:###
								
									if controlAt[0]==14:
										controlAt[0]=0
										controlAt[1]=controlAt[1]+1
									else:
										controlAt[0]=controlAt[0]+1 ##	
							else:###
								print('final')
								if controlAt[0]==14:
									controlAt[0]=0
									controlAt[1]=controlAt[1]+1
								else:
									controlAt[0]=controlAt[0]+1 #
									
									
					else:
						print('print cambio de orientacion') ### voy a cambiar la orientacion a horizontal
						if controlAt[1]+len(initial_atril2)-1<=14:
							L=True
							cont=0 ##aqui
							while L and(cont<len(initial_atril2)):
								if boardConfig[controlAt[0]][controlAt[1]+cont].get_estado() == True:
									L=False
									print('lugar ocupado ',controlAt)
								else:
									cont=cont+1 #aqui
							
							cont=0
							if L:
								y=controlAt[1]
								for i in range(len(initial_atril2)):
									y=y+cont
									cont=1
									B=(controlAt[0],y)
									piece_image=images[initial_atril2[i]]
									img=piece_image['imagen']
									window[B].update(image_filename=img, image_size= tamaño_img ,button_color=('white','red'))								
									#window[B].update(initial_atril2[i])
									boardConfig[controlAt[0]][y].set_estado(True) ##aqui
								if controlAt[0]==14:
									controlAt[0]=0
									controlAt[1]=controlAt[1]+1
								else:
									controlAt[0]=controlAt[0]+1 #aqui
								T=False#aquizzz
							else: ### lugar ocupado
								print('FF0')					
								if controlAt[0]==14:
									controlAt[0]=0
									controlAt[1]=controlAt[1]+1
								else:
									controlAt[0]=controlAt[0]+1##aqui
						else:
							print('la palabra no entro con la orientacion horizontal')
							if controlAt[0]==14:
								controlAt[0]=0
								controlAt[1]=controlAt[1]+1
							else:
								controlAt[0]=controlAt[0]+1
							print(controlAt)#zzz
		
				if(controlAt[1]==15):
					print('final')
					print(controlAt)
					#VF[0]=False	
		
			# D=random.randint(0,2)
			
			# if D==0:
				# initial_atril2=['h','o','l','a']
			# elif D==1:
				# initial_atril2=['c','o','m','o']
			# else:
				# initial_atril2=['e','s','t','a','n']
			# if VF[1]==0:
				# VF[1]=VF[1]+1
				# opc=random.randint(0,1)
				# VF[2]=opc
			# if VF[1]==1:
				# if (VF[2]==0):
					# print('VERTICAL')
					# vertical()
				# else:
					# print('HORIZONTAL')
					# horizontal()
		#######
			if controlAt[2]==0:
				controlAt[2]=controlAt[2]+1
				opc=random.randint(0,1)
				controlAt[3]=opc
			if controlAt[2]==1:
				if (controlAt[3]==0):
					print('VERTICAL')
					vertical()
				else:
					print('HORIZONTAL')
					horizontal()
		def comprobarPalabra(palabra):
			#ll[0]='zzzzz'
			T=False
		
			if not palabra.lower() in verbs:
				
				if not palabra.lower() in spelling:
					
					
					if (not(palabra.lower() in lexicon) and not(palabra.upper() in lexicon) and not(palabra.capitalize() in lexicon)):
						
					#print('no existe la palabra')
						#sg.Popup('la palabra no existe')
						T=False
					else:
						T=True
						#sg.Popup('la palabra existe')
					
				else:
					#print('existe')
					#print(palabra)
					T=True
					
					#sg.Popup('la palabra existe')		
					
			else:
				#print('existe')
				#print(palabra)
				T=True
				#sg.Popup('la palabra existe')	
			return T
					
		A = ["a", "b", "c"]
		ll=['hola']
		# StrA = "".join(A)
		# print(StrA)
		cadena =['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','Y','Z','X']
		
		# for c in combinations(cadena,4):
			# print(c)
			# STRA="".join(c)
			# print(STRA)
			
		initial_atril=[]
		for i in range(0,7):
			initial_atril.append(random.choice(cadena))	
		
		#print(initial_atril)
		
		# for c in combinations(initial_atril,2):
			# lt="".join(c)
			# #lt='de'
			# #print(lt.capitalize())
			# #print(lt)
			# if(comprobarPalabra(lt)):
				# print('palabra valida',lt)
			
		#print(ll[0])
		listaPalabras=[]
		cont3=7
		nivel=3 ## pasar como parametro
		T=True
		while T and 2<=cont3:
			listaPalabras=[]
			#print('*'*30)
			for c in combinations(initial_atril,cont3):
				lp="".join(c)
				#print(lp)
				listaPalabras.append(lp)
			#cont3=cont3-1
			#print(listaPalabras)
			cont=len(listaPalabras)
			cont2=0
			# T=True
			while cont!=cont2 and T:
				
				
				# if(comprobarPalabra(listaPalabras[cont2])):
					# #print('existe')
					# #print(listaPalabras[cont2])
					# L=parse(listaPalabras[cont2]).split()
					# #print(L[0][0][1])
					# if L[0][0][1]=='VB':
						# print(listaPalabras[cont2])
						# print(parse(listaPalabras[cont2]).split())
						# T=False
				if nivel==3:
					nivel=random.randint(1,2)
					print('nivel',nivel)
				if nivel==1:
					if(comprobarPalabra(listaPalabras[cont2])):
						print(listaPalabras[cont2],'EXISTE')
						T=False
						IA(listaPalabras[cont2])
						
				if nivel==2:
					if(comprobarPalabra(listaPalabras[cont2])):
						L=parse(listaPalabras[cont2]).split()
						if L[0][0][1]=='VB' or L[0][0][1] =='JJ':
							print(listaPalabras[cont2])
							print(parse(listaPalabras[cont2]).split())
							T=False
							IA(listaPalabras[cont2])
		
					
						
						
					#T=False
				cont2=cont2+1
				
				
				if cont==cont2:
					cont3=cont3-1
				
		if cont3<2:
			sg.Popup('LA IA NO PUDO FORMAR UNA PALABRA VALIDA ')		


###################
	for i in range(0,7):
		initial_atril.append(random.choice(images_keys))	
		
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
			p2=palabra[0]
			p2=p2+letra
			palabra[0]=p2
			initial_atril[i]='' ## relacionar con la bolsa
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
			
		

	# def BorrarTablero1(color):### algo que no  vi cuando estaba haciendo el tablero , es el hecho de blanquear el tablero cuando ocurra el evento pasar , si tengo 3 tablero debo repetir 3 veces este metodo 
		# if color == 'green':
			# piece_image = images_PuntosNv1['LX2']
			# #row.append(self.render_square(piece_image,key =(i,j),texto='', color_button=('white','green')))
			# window[(i,j)].update(image_filename=piece_image, image_size= tamaño_img ,button_color=('white','green'))
		
		# elif color == 'red':
			# piece_image = images_PuntosNv1['PX3']
			# #row.append(self.render_square(piece_image,key =(i,j),texto='', color_button=('white','red')))
			

			# window[(i,j)].update(image_filename=piece_image, image_size= tamaño_img ,button_color=('white','red'))
		# elif color == 'blue':
			# piece_image = images_PuntosNv1['LX3']
			# #row.append(self.render_square(piece_image,key =(i,j),texto='', color_button=('white','blue')))
			# window[(i,j)].update(image_filename=piece_image, image_size= tamaño_img ,button_color=('white','blue'))
		# elif color == 'violet':
			# piece_image=os.path.join(base_path,'images/corona.png')
			# #row.append(self.render_square(piece_image,key =(i,j),texto='', color_button=('white','white')))
			# window[(i,j)].update(image_filename=piece_image, image_size= tamaño_img ,button_color=('white','white'))												
		# elif color == 'orange':
			# piece_image = images_PuntosNv1['PX2']
			# #row.append(self.render_square(piece_image,key =(i,j),texto='', color_button=('white','orange')))
			# window[(i,j)].update(image_filename=piece_image, image_size= tamaño_img ,button_color=('white','orange'))
						
		# else:
			# #color_button=('white','white')
			# piece_image = images['BLANK']
			# piece_image = piece_image['imagen']
			# #row.append(self.render_square(piece_image['imagen'],key =(i,j),texto='')) 
			# window[(i,j)].update(image_filename=piece_image, image_size= tamaño_img ,button_color=('white','white'))
			

	# def BorrarTablero2(color):### algo que no  vi cuando estaba haciendo el tablero , es el hecho de blanquear el tablero cuando ocurra el evento pasar , si tengo 3 tablero debo repetir 3 veces este metodo 
		# if color == 'green':
			# piece_image = images_PuntosNv1['LX2']
			# #row.append(self.render_square(piece_image,key =(i,j),texto='', color_button=('white','green')))
			# window[(i,j)].update(image_filename=piece_image, image_size= tamaño_img ,button_color=('white','green'))
		
		# elif color == 'red':
			# piece_image = images_PuntosNv1['PX3']
			# #row.append(self.render_square(piece_image,key =(i,j),texto='', color_button=('white','red')))
			

			# window[(i,j)].update(image_filename=piece_image, image_size= tamaño_img ,button_color=('white','red'))
		# elif color == 'blue':
			# piece_image = images_PuntosNv1['LX3']
			# #row.append(self.render_square(piece_image,key =(i,j),texto='', color_button=('white','blue')))
			# window[(i,j)].update(image_filename=piece_image, image_size= tamaño_img ,button_color=('white','blue'))
		# elif color == 'violet':
			# piece_image=os.path.join(base_path,'images/centro.png')
			# #row.append(self.render_square(piece_image,key =(i,j),texto='', color_button=('white','white')))
			# window[(i,j)].update(image_filename=piece_image, image_size= tamaño_img ,button_color=('white','Dark violet'))												
		# elif color == 'orange':
			# piece_image = images_PuntosNv1['PX2']
			# #row.append(self.render_square(piece_image,key =(i,j),texto='', color_button=('white','orange')))
			# window[(i,j)].update(image_filename=piece_image, image_size= tamaño_img ,button_color=('white','orange'))
						
		# else:
			# #color_button=('white','white')
			# piece_image = images['BLANK']
			# piece_image = piece_image['imagen']
			# #row.append(self.render_square(piece_image['imagen'],key =(i,j),texto='')) 
			# window[(i,j)].update(image_filename=piece_image, image_size= tamaño_img ,button_color=('white','white'))











			
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
	atr1=atril1(True).crearAtril()
	atr2=atril1(False).crearAtril()
	if num_tablero ==1:
		obj = Tablero1()
	elif num_tablero == 2:
		obj = Tablero2()		
	elif num_tablero ==3:
		obj = Tablero3()
	bolsa.repartir(14)		

	opc=1 # 2 para borrar el tablero 2 , 3 para el tablero 3 se tiene que elegir cuando se elige el tablero
	print('*')
	boardConfig=config_tablero.Config1() ## para enganchar con el menu existen 3 configuraciones
	#boardConfig=config_tablero.Config2() casillas naranjas descuentan puntos por palabra x-2
	##boardConfig=config_tablero.Config3 () verde y azul quitan puntos

	elementos=obj.Tab(images) ##### estaria para conectarlo con una opcion para elegir el tablero
	tablero= elementos[0] 
	tamaño_img = elementos[1]

	columna_2 = [ [sg.Text('PUNTOS MAQUINA')],[sg.Listbox(values =[], key='datosm', font='Courier 18' ,size=(20,10))],[sg.Text('TOTAL PUNTOS')],[sg.Text('FICHAS RESTANTES', size=(20, 2), justification='center')],[sg.Text(str(bolsa.get_fichas_restantes()) , size=(20, 2), justification='center')],]
	columna_1 = [ [sg.Text('PUNTOS JUGADOR')],[sg.Listbox(values =[], key='datosj', font='Courier 18',size=(20,10))],[sg.Text('TOTAL PUNTOS')]]
	columna_3 = [ [sg.Text('Total Puntos')]]				
	


	board_tab=[[sg.Button('CHECK')],[sg.Column(columna_1),sg.Column(atr1),sg.Column(tablero),sg.Column(atr2),sg.Column(columna_2)],[sg.Button('COMENZAR'),sg.Button('PASAR'),sg.Button('GUARDAR'),sg.Button('EXIT')]]
	window = sg.Window('ScrabbleAr',default_button_element_size=(10,1), auto_size_buttons=False).Layout(board_tab)
	cantPasadas=0
	#palabra=''	
	
	palabra=['']
	#i=0
	cant=4
	T5=True
	T1=True
	T2= True
	T3= True
	T4= True
	F=0
	C=0
	#x=0
	puntosCasilla=[]
	putosL=0

	listado=[]
	inicio=time.time()
	while True:
		
		while True:
			puntosP=0
			puntosL=0
			letra=''
			l=-1
			button , value = window.Read()
			if button == 'CHECK':
				
				#T5=False
				#obj_tablero.get_word()
				if palabra == '':
					sg.Popup('todavia no formo una palabra')
				elif len(palabra[0])>1:
					
					if chequearPalabra.comprobarPalabraEnBaseAlNivel(palabra[0]):
						print('palabraValida')
					print(palabra[0])
					sg.Popup('PALABRA FORMADA : ' ,palabra)
					
					palabra[0]=''
					T2= True
					T1=True
					#T3= True
					F=0
					C=0
					cant=cant+1
					#x=0
					T4=True
					#T5=False
					break
					##window[]
				# if len(word)>= 2 and len(word) <=7:
				elif len(palabra[0])<2:
					sg.Popup('la palabra es menor de 2')
					break
								
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
					# for i in range(15):
						# for j in range(15):
							# window[(i,j)].update('')
							# boardConfig[i][j].set_estado(False)
							# color=boardConfig[i][j].get_color()
							# BorrarTablero1(color)
				else:
					sg.Popup('se supero la cantidad de pasadas')
				cant=4
				T1=True
				T2=True
				T3=True
				palabra=['']
				listado=[]
				actualizar_listado(window.FindElement('datosj'))
				#T5=False
				break
				
	
				
					
			if type(button) is int:
				print(button)
				
				if initial_atril[button] !='':
					i=button
					letra= initial_atril[button]
					#####hoy palabra += letra
	
					button , value = window.Read()
					if type(button) is tuple:
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
						if cant<4: ## la cantidad de palabras formadas con 7 letras
		
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
		
		
		inteligenia()
		final=time.time()
		if final-inicio>60:
			break		
		
	# while True:
		# puntosP=0
		# puntosL=0
		# letra=''
		# l=-1
		# button , value = window.Read()
		# if button == 'CHECK':
			# #obj_tablero.get_word()
			# if palabra == '':
				# sg.Popup('todavia no formo una palabra')
			# elif len(palabra[0])>1:
				# print(palabra[0])
				# sg.Popup('PALABRA FORMADA : ' ,palabra)
				
				# palabra[0]=''
				# T2= True
				# T1=True
				# #T3= True
				# F=0
				# C=0
				# cant=cant+1
				# #x=0
				# T4=True
				# ##window[]
			# # if len(word)>= 2 and len(word) <=7:
			# elif len(palabra[0])<2:
				# sg.Popup('la palabra es menor de 2')			
		# if button in (None , 'EXIT'):
			# exit()

			
			
			
		# if button =='PASAR':
			# cantPasadas=cantPasadas+1
			# if cantPasadas<4:
		
				# initial_atril=[]
				# for i in range(0,7): ##cambiar i
					# initial_atril.append(random.choice(images_keys))
				# for i in range(7):
					# #window[i].update(initial_atril[i])
					# piece_image = images[initial_atril[i]]
									
					# img=piece_image['imagen']

					# window[i].update(image_filename=img,image_size=(50, 50), button_color=('',''))
		# ##### blanquear tablero
		
		
				# actulizarTablero(opc)
				# # for i in range(15):
					# # for j in range(15):
						# # window[(i,j)].update('')
						# # boardConfig[i][j].set_estado(False)
						# # color=boardConfig[i][j].get_color()
						# # BorrarTablero1(color)
			# else:
				# sg.Popup('se supero la cantidad de pasadas')
			# cant=4
			# T1=True
			# T2=True
			# T3=True
			# palabra=['']
			# listado=[]
			# actualizar_listado(window.FindElement('datosj'))

			
				
		# if type(button) is int:
			# print(button)
			
			# if initial_atril[button] !='':
				# i=button
				# letra= initial_atril[button]
				# #####hoy palabra += letra

				# button , value = window.Read()
				# if type(button) is tuple:
					# if (button[0]==7 and button[1]==7)and T3 :
						# print(button)
						# modificarBoton()
						# T3=False
						# F=button[0]
						# C=button[1]
						# cant=0
					# #print(type(lista[1]))
					# if not(T3):
						# if(button[0]==F)and T1:
							# if C<button[1]:
								# T2=False
								# modificarBoton()
								# C=button[1]
						# if(button[1]==C)and T2:
							# if F<button[0]:
								# print(button)
								# T1=False
								# modificarBoton()
								# F=button[0]	
					# if cant<4: ## la cantidad de palabras formadas con 7 letras
	
						# if T4:
							# #x=x+1
							# modificarBoton()
							# F=button[0]
							# C=button[1]
							# T4=False
						# else:
							# if(button[0]==F)and T1:
								# if C<button[1]:
									# T2=False
									# modificarBoton()
									# C=button[1]
							# if(button[1]==C)and T2:
								# if F<button[0]:
									# T1=False
									# modificarBoton()
									# F=button[0]				
								
					# ## puntos mostrar por letra o palabra solo voy a mostar los puntos por las casillas
					
					# actualizar_listado(window.FindElement('datosj')) ## habria que multiplicar el valor de cada letra o palabra

					# ## modifiquenlo para que muestres los puntos que se van acumulando por casillas 
					# ##
																
					# l=0
	
			
			
		# if type(button) is tuple:
			# if l ==-1:
				
				# sg.Popup('movimiento incorrecto')			
			
main_game(1)			


