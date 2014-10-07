from numpy import *
import funciones
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
ganar = evitar
while ganar == evitar:
        ganar=int(raw_input("Ingrese casilla a la cual desea llegar:"))
if ganar<5:
        matriz[1,ganar]='G'
        gana=(1,ganar)
elif ganar<9:
        matriz[2,ganar-4]='G'
        gana=(2,ganar-4)
else:
        matriz[3,ganar-8]='G'
        gana=(3,ganar-8)
muro = ganar
while muro == ganar or muro == evitar:
        muro=int(raw_input("Ingrese casilla no accesible:"))
if muro<5:
        matriz[1,muro]='M'
elif muro<9:
        matriz[2,muro-4]='M'
else:
        matriz[3,muro-8]='M'
inicio = ganar
while inicio == ganar or inicio == muro or inicio == evitar:
        inicio=int(raw_input("Ingrese casilla de inicio:"))
if inicio<5:
        matriz[1,inicio]='I'
elif inicio<9:
        matriz[2,inicio-4]='I'
else:
        matriz[3,inicio-8]='I'
fil,col=gana
if fil==1:
	if matriz[2,col]=='B':
		matriz[2,col]='N'
		if matriz[2,col+1]=='B':
			matriz[2,col+1]='O'
		if matriz[2,col-1]=='B':
			matriz[2,col-1]='E'
		if matriz[3,col]=='B':
			matriz[3,col]='N'
			if matriz[3,col+1]=='B':
				matriz[3,col+1]='O'
			if matriz[3,col-1]=='B':
				matriz[3,col-1]='E'
if fil==2:
	if matriz[1,col]=='B':
		matriz[1,col]='S'
		if matriz[1,col+1]=='B':
			matriz[1,col+1]='O'
		if matriz[1,col-1]=='B':
			matriz[1,col-1]='E'
	if matriz[3,col]=='B':
		matriz[3,col]='N'
		if matriz[3,col+1]=='B':
			matriz[3,col+1]='O'
		if matriz[3,col-1]=='B':
			matriz[col-1]='E'
if fil==3:
	if matriz[2,col]=='B':
		matriz[2,col]='S'
		if matriz[2,col+1]=='B':
			matriz[2,col+1]='O'
		if matriz[2,col-1]=='B':
			matriz[2,col-1]='E'
		if matriz[1,col]=='B':
			matriz[1,col]='S'
			if matriz[1,col+1]=='B':
				matriz[1,col+1]='O'
			if matriz[1,col-1]=='B':
				matriz[1,col-1]='E'
if col==1:
	if matriz[fil,2]=='B':
		matriz[fil,2]='O'
		if matriz[fil+1,2]=='B':
			matriz[fil+1]='N'
		if matriz[fil-1,2]=='B':
			matriz[fil-1,2]='S'
		if matriz[fil,3]=='B':
			matriz[fil,3]='O'
			if matriz[fil+1,3]=='B':
				matriz[fil+1,3]='N'
			if matriz[fil-1,3]=='B':
				matriz[fil-1,3]='S'
			if matriz[fil,4]=='B':
				matriz[fil,4]='O'
				if matriz[fil+1,4]=='B':
					matriz[fil+1,4]='N'
				if matriz[fil-1,4]=='B':
					matriz[fil-1,4]='S'
