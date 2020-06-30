from pattern.es import parse, split

def clasificarPalabraPattern(palabra):
    '''
    clasifica el string recibido como paramentro en pattern, analizando la palabra, devuleve su clasificacion
    (sustantivo, adjetivo o verbo).
    '''
    s = parse(palabra).split()
    encontre = '9999'
    try:
        for cada in s:
            for i in cada:
                if i[1] == 'VB':
                    encontre = 'VB'
                    return encontre
                elif i[1] == 'NN':
                    encontre = 'NN'
                    return encontre
                elif i[1] == 'JJ':
                    encontre = 'JJ'
                    return encontre
    except(AttributeError):
        return 'No se pudo clasificar'

listaSustantivos = []
listaAdjetivos = []
listaVerbos = []

def clasificacionPattern(p):
	try:
		if clasificarPalabraPattern(p) == 'NN':
			listaSustantivos.append(p)
		elif clasificarPalabraPattern(p) == 'JJ':
			listaAdjetivos.append(p)
		elif clasificarPalabraPattern(p) == 'VB':
			listaVerbos.append(p)
		else:
			    print('No se pudo agregar')
            
	except(AttributeError):
		print('No se pudo agregar')

#====================PRUEBAS====================
# t = input('ingrese una palabra ')
# while t != 'z':
#     print(clasificarPalabraPattern(t))
#     clasificacionPattern(t)
#     t = input('ingrese una palabra ')

# print(listaSustantivos)
# print(listaVerbos)
# print(listaAdjetivos)
#===============================================


