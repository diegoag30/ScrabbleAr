
tablero=[]
for i in range(15):  ### tablero botones
	row=[]
	for j in range(15):
		dic={'ocup':False,'valor':False,'color':'','palabra':False,'letra':False,'puntosx':0}
		lista=[j]
		if j==3:
			lista.append('modulo')
		elif j==9:
			lista.append('modulo2')
			
		# piece_image = images['BLANK']
		# if j== 8 and i ==8:
			# row.append(render_square(im2,key = (i,j)))
		# else:
		row.append(dic)	
	tablero.append(row)
#print(tablero)
#print(tablero[0][3][0:])### revisar
#### colores matriz
# print(tablero[7][7])
# dic={'boolean':True,'color':'green','puntos':0}
# tablero[7][7].append(dic)

#print(tablero[7][7])
#print(tablero[7][7][1])
###
# def centro():
	# dic={'ocup':False,'valor':True,'color':'violet','palabra':False,'letra':False,'puntosx':0}

	# tablero[7][7]=dic
	#print(tablero[7][7])
### naranja
def naranja():
	dic={'ocup':False,'valor':True,'color':'orange','palabra':False,'letra':False,'puntosx':2}
	tablero[1][1]=dic	
	tablero[2][2]=dic
	tablero[3][3]=dic
	tablero[4][4]=dic
	tablero[10][10]=dic
	tablero[11][11]=dic
	tablero[12][12]=dic
	tablero[13][13]=dic
	
	tablero[1][13]=dic
	tablero[2][12]=dic
	tablero[3][11]=dic
	tablero[4][10]=dic
	
	tablero[10][4]=dic
	tablero[11][3]=dic
	tablero[12][2]=dic
	tablero[13][1]=dic
	
def centro():
	dic={'ocup':False,'valor':True,'color':'violet','palabra':False,'letra':False,'puntosx':0}

	tablero[7][7]=dic	
def rojo():
	
	dic={'ocup':False,'valor':True,'color':'red','palabra':True,'letra':False,'puntosx':3}
	tablero[0][0]=dic
	tablero[0][7]=dic
	tablero[0][14]=dic
	tablero[14][7]=dic
	tablero[14][14]=dic
	tablero[7][14]=dic
	tablero[7][0]=dic
	tablero[14][0]=dic	
	
naranja()
centro()
rojo()
