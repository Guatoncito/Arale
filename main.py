from numpy import *
matriz=array([['B','B','B','B','B','B'],
	          ['B','B','B','B','B','B'],
	          ['B','B','B','B','B','B'],
	          ['B','B','B','B','B','B'],
	          ['B','B','B','B','B','B']])
evitar=int(raw_input("Ingrese casilla para evitar:"))
if evitar<5:
        matriz[1,evitar]='P'
elif evitar<9:
        matriz[2,evitar-4]='P'
else:
        matriz[3,evitar-8]='P'
ganar=int(raw_input("Ingrese casilla a la cual desea llegar:"))
if ganar<5:
        matriz[1,ganar]='G'
        gana=(1,ganar)
elif evitar<9:
        matriz[2,ganar-4]='G'
        gana=(2,ganar-4)
else:
        matriz[3,ganar-8]='G'
        gana=(3,ganar-8)
muro=int(raw_input("Ingrese casilla no accesible:"))
if muro<5:
        matriz[1,perder]='M'
elif muro<9:
        matriz[2,perder-4]='M'
else:
        matriz[3,perder-8]='M'
inicio=int(raw_input("Ingrese casilla de inicio:"))
if inicio<5:
        matriz[1,inicio]='I'
elif inicio<9:
        matriz[2,inicio-4]='I'
else:
        matriz[3,inicio-8]='I'

