import PySimpleGUI as sg
from itertools import combinations
import random

##import configuracion
from pattern.es import verbs, tag, spelling, lexicon
import string
from pattern.es import singularize , pluralize, conjugate , INFINITIVE , PRESENT , PAST , SG , PERFECTIVE , SUBJUNCTIVE ,PL ,parse
import os.path
base_path=os.path.dirname(os.path.abspath(__file__))

def saludo():
	print('hola fer')
	
def inteligencia(controlAt,window,boardConfig,images):
		
	def IA(initial_atril2):
            # piece_image = images[initial_atril[i]]
			# img=piece_image['imagen']
			# window[button].update(image_filename=img, image_size= tamaño_img ,button_color=('white','grey'))		
		controlAt[0]=random.randint(0,14)
		controlAt[1]=random.randint(0,14)
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
						print('lugares ocupados')### ### trato de escribir en horizontal
						print(controlAt)
						if controlAt[1]+len(initial_atril2)-1<=14:
							L=True
							cont=0
							while L and (cont<len(initial_atril2)):##
								if boardConfig[controlAt[0]][controlAt[1]+cont].get_estado() == True:
									L=False
									print('lugar ocupado')
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
					print('cambio de orientacion') ### voy a cambiar la orientacion a horizontal
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
		#sg.Popup('LA IA NO PUDO FORMAR UNA PALABRA VALIDA ')
		print('LA IA NO PUDO FORMAR UNA PALABRA VALIDA ')		
	
	
	
	
	
	
	
	
	
	
	

