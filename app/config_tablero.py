class EstadBoton:
	'''Esta clase maneja la configuracion del tablero,
	 ya sea el valor de las casillas, los colores, y el estado de los botones '''
	def __init__(self,valor=1,color='',estado=False,tipo='L'): # valor es 1 por defecto para multiplicar la L o P
		self._estado = estado
		self._valor = valor
		self._color = color
		self._tipo = tipo
	def get_color(self):
		return self._color
	def get_valor(self):
		return self._valor		
	def get_estado(self):
		return self._estado
	def get_tipo(self):
		return self._tipo
	def set_estado(self,valor):
		self._estado=valor
						
def Config1():
	configuracion1=[]
	#row=[]
	for i in range(15):
		row=[]
		for j in range(15):
			row.append(EstadBoton())
		configuracion1.append(row)
	configuracion1[7][7]=EstadBoton(1,'violet',tipo='P')
	configuracion1[1][1]=EstadBoton(2,'orange',tipo='P')	
	configuracion1[2][2]=EstadBoton(2,'orange',tipo='P')	
	configuracion1[3][3]=EstadBoton(2,'orange',tipo='P')	
	configuracion1[4][4]=EstadBoton(2,'orange',tipo='P')	
	configuracion1[10][10]=EstadBoton(2,'orange',tipo='P')	
	configuracion1[11][11]=EstadBoton(2,'orange',tipo='P')	
	configuracion1[12][12]=EstadBoton(2,'orange',tipo='P')	
	configuracion1[13][13]=EstadBoton(2,'orange',tipo='P')	
	configuracion1[1][13]=EstadBoton(2,'orange',tipo='P')	
	configuracion1[2][12]=EstadBoton(2,'orange',tipo='P')	
	configuracion1[3][11]=EstadBoton(2,'orange',tipo='P')	
	configuracion1[4][10]=EstadBoton(2,'orange',tipo='P')	
	configuracion1[10][4]=EstadBoton(2,'orange',tipo='P')	
	configuracion1[11][3]=EstadBoton(2,'orange',tipo='P')
	configuracion1[12][2]=EstadBoton(2,'orange',tipo='P')	
	configuracion1[13][1]=EstadBoton(2,'orange',tipo='P')	
	

	
	configuracion1[0][0]=EstadBoton(1,'red',tipo='P')	
	configuracion1[0][7]=EstadBoton(3,'red',tipo='P')
	configuracion1[0][14]=EstadBoton(3,'red',tipo='P')
	configuracion1[14][7]=EstadBoton(3,'red',tipo='P')
	configuracion1[14][14]=EstadBoton(3,'red',tipo='P')
	configuracion1[7][14]=EstadBoton(3,'red',tipo='P')
	configuracion1[7][0]=EstadBoton(3,'red',tipo='P')
	configuracion1[14][0]=EstadBoton(3,'red',tipo='P')
	configuracion1[7][7]=EstadBoton(0,'violet',tipo='P')
	
	configuracion1[1][5]=EstadBoton(3,'blue',tipo='L')
	configuracion1[1][9]=EstadBoton(3,'blue',tipo='L')
	configuracion1[5][1]=EstadBoton(3,'blue',tipo='L')
	configuracion1[5][5]=EstadBoton(3,'blue',tipo='L')
	configuracion1[5][9]=EstadBoton(3,'blue',tipo='L')
	configuracion1[5][13]=EstadBoton(3,'blue',tipo='L')
	configuracion1[9][5]=EstadBoton(3,'blue',tipo='L')
	configuracion1[9][9]=EstadBoton(3,'blue',tipo='L')
	configuracion1[9][13]=EstadBoton(3,'blue',tipo='L')
	configuracion1[13][5]=EstadBoton(3,'blue',tipo='L')
	configuracion1[13][9]=EstadBoton(3,'blue',tipo='L')
	configuracion1[9][1]=EstadBoton(3,'blue',tipo='L')
	configuracion1[0][3]=EstadBoton(2,'green',tipo='L')
	configuracion1[0][11]=EstadBoton(2,'green',tipo='L')
	configuracion1[2][6]=EstadBoton(2,'green',tipo='L')
	configuracion1[2][8]=EstadBoton(2,'green',tipo='L')
	configuracion1[3][0]=EstadBoton(2,'green',tipo='L')
	configuracion1[3][7]=EstadBoton(2,'green',tipo='L')
	configuracion1[3][14]=EstadBoton(2,'green',tipo='L')
	configuracion1[6][2]=EstadBoton(2,'green',tipo='L')
	configuracion1[6][6]=EstadBoton(2,'green',tipo='L')
	configuracion1[6][8]=EstadBoton(2,'green',tipo='L')
	configuracion1[6][12]=EstadBoton(2,'green',tipo='L')
	configuracion1[7][3]=EstadBoton(2,'green',tipo='L')
	configuracion1[7][11]=EstadBoton(2,'green',tipo='L')
	configuracion1[8][2]=EstadBoton(2,'green',tipo='L')
	configuracion1[8][6]=EstadBoton(2,'green',tipo='L')
	configuracion1[8][8]=EstadBoton(2,'green',tipo='L')
	configuracion1[8][12]=EstadBoton(2,'green',tipo='L')
	configuracion1[11][0]=EstadBoton(2,'green',tipo='L')
	configuracion1[11][7]=EstadBoton(2,'green',tipo='L')
	configuracion1[11][14]=EstadBoton(2,'green',tipo='L')
	configuracion1[12][6]=EstadBoton(2,'green',tipo='L')
	configuracion1[12][8]=EstadBoton(2,'green',tipo='L')
	configuracion1[14][3]=EstadBoton(2,'green',tipo='L')
	configuracion1[14][11]=EstadBoton(2,'green',tipo='L')																																														
	
	
	
	return configuracion1
	
	
	
	
	
def Config2():
	configuracion1=[]
	#row=[]
	for i in range(15):
		row=[]
		for j in range(15):
			row.append(EstadBoton())
		configuracion1.append(row)
	#configuracion1[7][7]=EstadBoton(1,'B')
	configuracion1[1][1]=EstadBoton(-2,'orange',tipo='P')	
	configuracion1[2][2]=EstadBoton(-2,'orange',tipo='P')	
	configuracion1[3][3]=EstadBoton(-2,'orange',tipo='P')	
	configuracion1[4][4]=EstadBoton(-2,'orange',tipo='P')	
	configuracion1[10][10]=EstadBoton(-2,'orange',tipo='P')	
	configuracion1[11][11]=EstadBoton(-2,'orange',tipo='P')	
	configuracion1[12][12]=EstadBoton(-2,'orange',tipo='P')	
	configuracion1[13][13]=EstadBoton(-2,'orange',tipo='P')	
	configuracion1[1][13]=EstadBoton(-2,'orange',tipo='P')	
	configuracion1[2][12]=EstadBoton(-2,'orange',tipo='P')	
	configuracion1[3][11]=EstadBoton(-2,'orange',tipo='P')	
	configuracion1[4][10]=EstadBoton(-2,'orange',tipo='P')	
	configuracion1[10][4]=EstadBoton(-2,'orange',tipo='P')	
	configuracion1[11][3]=EstadBoton(-2,'orange',tipo='P')
	configuracion1[12][2]=EstadBoton(-2,'orange',tipo='P')	
	configuracion1[13][1]=EstadBoton(-2,'orange',tipo='P')	
	

	
	configuracion1[0][0]=EstadBoton(1,'red',tipo='P')	
	configuracion1[0][7]=EstadBoton(3,'red',tipo='P')
	configuracion1[0][14]=EstadBoton(3,'red',tipo='P')
	configuracion1[14][7]=EstadBoton(3,'red',tipo='P')
	configuracion1[14][14]=EstadBoton(3,'red',tipo='P')
	configuracion1[7][14]=EstadBoton(3,'red',tipo='P')
	configuracion1[7][0]=EstadBoton(3,'red',tipo='P')
	configuracion1[14][0]=EstadBoton(3,'red',tipo='P')
	configuracion1[7][7]=EstadBoton(0,'violet',tipo='P')
	
	configuracion1[1][5]=EstadBoton(3,'blue',tipo='L')
	configuracion1[1][9]=EstadBoton(3,'blue',tipo='L')
	configuracion1[5][1]=EstadBoton(3,'blue',tipo='L')
	configuracion1[5][5]=EstadBoton(3,'blue',tipo='L')
	configuracion1[5][9]=EstadBoton(3,'blue',tipo='L')
	configuracion1[5][13]=EstadBoton(3,'blue',tipo='L')
	configuracion1[9][5]=EstadBoton(3,'blue',tipo='L')
	configuracion1[9][9]=EstadBoton(3,'blue',tipo='L')
	configuracion1[9][13]=EstadBoton(3,'blue',tipo='L')
	configuracion1[13][5]=EstadBoton(3,'blue',tipo='L')
	configuracion1[13][9]=EstadBoton(3,'blue',tipo='L')
	configuracion1[9][1]=EstadBoton(3,'blue',tipo='L')
	configuracion1[0][3]=EstadBoton(2,'green',tipo='L')
	configuracion1[0][11]=EstadBoton(2,'green',tipo='L')
	configuracion1[2][6]=EstadBoton(2,'green',tipo='L')
	configuracion1[2][8]=EstadBoton(2,'green',tipo='L')
	configuracion1[3][0]=EstadBoton(2,'green',tipo='L')
	configuracion1[3][7]=EstadBoton(2,'green',tipo='L')
	configuracion1[3][14]=EstadBoton(2,'green',tipo='L')
	configuracion1[6][2]=EstadBoton(2,'green',tipo='L')
	configuracion1[6][6]=EstadBoton(2,'green',tipo='L')
	configuracion1[6][8]=EstadBoton(2,'green',tipo='L')
	configuracion1[6][12]=EstadBoton(2,'green',tipo='L')
	configuracion1[7][3]=EstadBoton(2,'green',tipo='L')
	configuracion1[7][11]=EstadBoton(2,'green',tipo='L')
	configuracion1[8][2]=EstadBoton(2,'green',tipo='L')
	configuracion1[8][6]=EstadBoton(2,'green',tipo='L')
	configuracion1[8][8]=EstadBoton(2,'green',tipo='L')
	configuracion1[8][12]=EstadBoton(2,'green',tipo='L')
	configuracion1[11][0]=EstadBoton(2,'green',tipo='L')
	configuracion1[11][7]=EstadBoton(2,'green',tipo='L')
	configuracion1[11][14]=EstadBoton(2,'green',tipo='L')
	configuracion1[12][6]=EstadBoton(2,'green',tipo='L')
	configuracion1[12][8]=EstadBoton(2,'green',tipo='L')
	configuracion1[14][3]=EstadBoton(2,'green',tipo='L')
	configuracion1[14][11]=EstadBoton(2,'green',tipo='L')																																														
	
	
	
	return configuracion1	
	
	
def Config3():
	configuracion1=[]
	#row=[]
	for i in range(15):
		row=[]
		for j in range(15):
			row.append(EstadBoton())
		configuracion1.append(row)
	#configuracion1[7][7]=EstadBoton(1,'Black violet')
	configuracion1[1][1]=EstadBoton(2,'orange',tipo='P')	
	configuracion1[2][2]=EstadBoton(2,'orange',tipo='P')	
	configuracion1[3][3]=EstadBoton(2,'orange',tipo='P')	
	configuracion1[4][4]=EstadBoton(2,'orange',tipo='P')	
	configuracion1[10][10]=EstadBoton(2,'orange',tipo='P')	
	configuracion1[11][11]=EstadBoton(2,'orange',tipo='P')	
	configuracion1[12][12]=EstadBoton(2,'orange',tipo='P')	
	configuracion1[13][13]=EstadBoton(2,'orange',tipo='P')	
	configuracion1[1][13]=EstadBoton(2,'orange',tipo='P')	
	configuracion1[2][12]=EstadBoton(2,'orange',tipo='P')	
	configuracion1[3][11]=EstadBoton(2,'orange',tipo='P')	
	configuracion1[4][10]=EstadBoton(2,'orange',tipo='P')	
	configuracion1[10][4]=EstadBoton(2,'orange',tipo='P')	
	configuracion1[11][3]=EstadBoton(2,'orange',tipo='P')
	configuracion1[12][2]=EstadBoton(2,'orange',tipo='P')	
	configuracion1[13][1]=EstadBoton(2,'orange',tipo='P')	
	

	
	configuracion1[0][0]=EstadBoton(1,'red',tipo='P')	
	configuracion1[0][7]=EstadBoton(3,'red',tipo='P')
	configuracion1[0][14]=EstadBoton(3,'red',tipo='P')
	configuracion1[14][7]=EstadBoton(3,'red',tipo='P')
	configuracion1[14][14]=EstadBoton(3,'red',tipo='P')
	configuracion1[7][14]=EstadBoton(3,'red',tipo='P')
	configuracion1[7][0]=EstadBoton(3,'red',tipo='P')
	configuracion1[14][0]=EstadBoton(3,'red',tipo='P')
	configuracion1[7][7]=EstadBoton(0,'violet',tipo='P')
	
	configuracion1[1][5]=EstadBoton(-3,'blue',tipo='L')
	configuracion1[1][9]=EstadBoton(-3,'blue',tipo='L')
	configuracion1[5][1]=EstadBoton(-3,'blue',tipo='L')
	configuracion1[5][5]=EstadBoton(-3,'blue',tipo='L')
	configuracion1[5][9]=EstadBoton(-3,'blue',tipo='L')
	configuracion1[5][13]=EstadBoton(-3,'blue',tipo='L')
	configuracion1[9][5]=EstadBoton(-3,'blue',tipo='L')
	configuracion1[9][9]=EstadBoton(-3,'blue',tipo='L')
	configuracion1[9][13]=EstadBoton(-3,'blue',tipo='L')
	configuracion1[13][5]=EstadBoton(-3,'blue',tipo='L')
	configuracion1[13][9]=EstadBoton(-3,'blue',tipo='L')
	configuracion1[9][1]=EstadBoton(-3,'blue',tipo='L')
	configuracion1[0][3]=EstadBoton(-2,'green',tipo='L')
	configuracion1[0][11]=EstadBoton(-2,'green',tipo='L')
	configuracion1[2][6]=EstadBoton(-2,'green',tipo='L')
	configuracion1[2][8]=EstadBoton(-2,'green',tipo='L')
	configuracion1[3][0]=EstadBoton(-2,'green',tipo='L')
	configuracion1[3][7]=EstadBoton(-2,'green',tipo='L')
	configuracion1[3][14]=EstadBoton(-2,'green',tipo='L')
	configuracion1[6][2]=EstadBoton(-2,'green',tipo='L')
	configuracion1[6][6]=EstadBoton(-2,'green',tipo='L')
	configuracion1[6][8]=EstadBoton(-2,'green',tipo='L')
	configuracion1[6][12]=EstadBoton(-2,'green',tipo='L')
	configuracion1[7][3]=EstadBoton(-2,'green',tipo='L')
	configuracion1[7][11]=EstadBoton(2,'green',tipo='L')
	configuracion1[8][2]=EstadBoton(-2,'green',tipo='L')
	configuracion1[8][6]=EstadBoton(-2,'green',tipo='L')
	configuracion1[8][8]=EstadBoton(-2,'green',tipo='L')
	configuracion1[8][12]=EstadBoton(-2,'green',tipo='L')
	configuracion1[11][0]=EstadBoton(-2,'green',tipo='L')
	configuracion1[11][7]=EstadBoton(-2,'green',tipo='L')
	configuracion1[11][14]=EstadBoton(-2,'green',tipo='L')
	configuracion1[12][6]=EstadBoton(-2,'green',tipo='L')
	configuracion1[12][8]=EstadBoton(-2,'green',tipo='L')
	configuracion1[14][3]=EstadBoton(-2,'green',tipo='L')
	configuracion1[14][11]=EstadBoton(-2,'green',tipo='L')																																														
	
	
	
	return configuracion1
	
	
	
	
	
	
	
	
	
	
	
	
	


