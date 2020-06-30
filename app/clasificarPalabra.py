from pattern.es import parse, split
from Configuracion import Configuracion
import random

def clasificarPalabraPattern(palabra):
    '''
    clasifica el string recibido como paramentro en pattern, analizando la palabra, devuleve su clasificacion
    (sustantivo(NN), adjetivo(JJ) o verbo(VB)).
    '''
    s = parse(palabra.lower()).split()
    try:
        for cada in s:
            for i in cada:
                if i[1] == 'VB':
                    tipo_palabra = 'VB'
                    return tipo_palabra
                elif i[1] == 'NN':
                    tipo_palabra = 'NN'
                    return tipo_palabra
                elif i[1] == 'JJ':
                    tipo_palabra = 'JJ'
                    return tipo_palabra
    except(AttributeError):
        return 'No se pudo clasificar'


#Esto lo tengo de prueba para algo a futuro
listaSustantivos = []
listaAdjetivos = []
listaVerbos = []

def clasificacionPattern(p):
	try:
		if clasificarPalabraPattern(p.lower()) == 'NN':
			listaSustantivos.append(p)
		elif clasificarPalabraPattern(p.lower()) == 'JJ':
			listaAdjetivos.append(p)
		elif clasificarPalabraPattern(p.lower()) == 'VB':
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

conf = Configuracion()

nivel = conf.getConfiguracionesSeleccionadas()['dificultad']

def comprobarPalabraEnBaseAlNivel(nivel,palabra='perro'):
    """
        devuelve True o False en base a la dificulad elegida en el menu de configuracion
    """
    if nivel == 'facil':
        if clasificarPalabraPattern(palabra) == 'NN' or clasificarPalabraPattern(palabra) == 'JJ' or clasificarPalabraPattern(palabra) == 'VB':
            return True
        else:
            return False
    elif nivel == 'normal':
        if clasificarPalabraPattern(palabra) == 'JJ' or clasificarPalabraPattern(palabra) == 'VB':
            return True
        else:
            return False
    else:
        if conf.getClasificacionSeleccionada() == 'JJ':
            if clasificarPalabraPattern(palabra) == 'JJ':
                return True
            else:
                return False
        if conf.getClasificacionSeleccionada() == 'VB':
            if clasificarPalabraPattern(palabra) == 'VB':
                return True
            else:
                return False

if __name__ == "__main__":
    #======================PRUEBAS======================
    # nivel = 'dificil'
    nivel = 'normal'
    palabra = 'correr'
    print(comprobarPalabraEnBaseAlNivel(nivel,palabra))
    


