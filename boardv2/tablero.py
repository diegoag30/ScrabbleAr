import PySimpleGUI as sg
import random
import coloresTablero
tab=coloresTablero.tablero
sg.ChangeLookAndFeel('Dark purple')

obj_tablero = Tablero()
obj_tablero.iniciar_tablero()

blank = {'letra':'', 'imagen': r'boardv2/blank.png'}
a={'letra':'A','imagen': r'boardv2/a.png'} #(r'img.png')
b={'letra':'B','imagen': r'boardv2/b.png'}
c={'letra':'C','imagen': r'boardv2/c.png'}
d={'letra':'D','imagen': r'boardv2/d.png'}
e={'letra':'E','imagen': r'boardv2/e.png'}
f={'letra':'F','imagen': r'boardv2/f.png'}
g={'letra':'G','imagen': r'boardv2/g.png'}
h={'letra':'H','imagen': r'boardv2/h.png'}
i={'letra':'I','imagen': r'boardv2/i.png'}
j={'letra':'J','imagen': r'boardv2/j.png'}
k={'letra':'K','imagen': r'boardv2/k.png'}
l={'letra':'L','imagen': r'boardv2/l.png'}
m={'letra':'M','imagen': r'boardv2/m.png'}
n={'letra':'N','imagen': r'boardv2/n.png'}
o={'letra':'O','imagen': r'boardv2/o.png'}
p={'letra':'P','imagen': r'boardv2/p.png'}
q={'letra':'Q','imagen': r'boardv2/q.png'}
r={'letra':'R','imagen': r'boardv2/r.png'}
s={'letra':'S','imagen': r'boardv2/s.png'}
t={'letra':'T','imagen': r'boardv2/t.png'}
u={'letra':'U','imagen': r'boardv2/u.png'}
v={'letra':'V','imagen': r'boardv2/v.png'}
w={'letra':'W','imagen': r'boardv2/w.png'}
x={'letra':'X','imagen': r'boardv2/x.png'}
y={'letra':'Y','imagen': r'boardv2/y.png'}
z={'letra':'Z','imagen': r'boardv2/z.png'}
im=r'boardv2/g.png'
img=r'boardv2/blank2.png'####
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
				corona=r'boardv2/corona.png'
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
inte=r'boardv2/interrogacion.png'
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
