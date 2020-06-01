import PySimpleGUI as sg
import random
sg.ChangeLookAndFeel('Dark purple')

blank = {'letra':'', 'imagen': r'blank.png'}
a={'letra':'A','imagen': r'a.png'} #(r'img.png')
b={'letra':'B','imagen': r'b.png'}
c={'letra':'C','imagen': r'c.png'}
d={'letra':'D','imagen': r'd.png'}
e={'letra':'E','imagen': r'e.png'}
f={'letra':'F','imagen': r'f.png'}
g={'letra':'G','imagen': r'g.png'}
h={'letra':'H','imagen': r'h.png'}
i={'letra':'I','imagen': r'i.png'}
j={'letra':'J','imagen': r'j.png'}
k={'letra':'K','imagen': r'k.png'}
l={'letra':'L','imagen': r'l.png'}
m={'letra':'M','imagen': r'm.png'}
n={'letra':'N','imagen': r'n.png'}
o={'letra':'O','imagen': r'o.png'}
p={'letra':'P','imagen': r'p.png'}
q={'letra':'Q','imagen': r'q.png'}
r={'letra':'R','imagen': r'r.png'}
s={'letra':'S','imagen': r's.png'}
t={'letra':'T','imagen': r't.png'}
u={'letra':'U','imagen': r'u.png'}
v={'letra':'V','imagen': r'v.png'}
w={'letra':'W','imagen': r'w.png'}
x={'letra':'X','imagen': r'x.png'}
y={'letra':'Y','imagen': r'y.png'}
z={'letra':'Z','imagen': r'z.png'}
im=r'g.png'
img=r'blank2.png'####
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
window = sg.Window('ScrabbleAr',default_button_element_size=(10,2), auto_size_buttons=False).Layout(board_tab)
#indow = sg.Window('tablero', layout, default_button_element_size=(5,2), auto_size_buttons=False)
#event, value = window.Read()
palabra=''
while True:
	letra=''
	l=-1
	button , value = window.Read()
	if button == 'CHECK':
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
				l=0
			# piece_image = images['BLANK']
		# row.append(render_square(piece_image['imagen'],key = (i,j)))	
		
		
		
	if type(button) is tuple:
		if l ==-1:
			
			sg.Popup('movimiento incorrecto')
