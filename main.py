from numpy import *
from funciones import *
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
fil,col=gana
matriz=directo(matriz)
if fil==1:
	matriz=magia(matriz,(fil,col),'E')
	matriz=magia(matriz,(fil,col),'O')
	matriz=magia(matriz,(fil+1,col),'E')
	matriz=magia(matriz,(fil+1,col),'O')
	matriz=magia(matriz,(fil+2,col),'E')
	matriz=magia(matriz,(fil+2,col),'O')
elif fil==2:
	matriz=magia(matriz,(fil,col),'E')
	matriz=magia(matriz,(fil,col),'O')
	matriz=magia(matriz,(fil+1,col),'E')
	matriz=magia(matriz,(fil+1,col),'O')
	matriz=magia(matriz,(fil-1,col),'E')
	matriz=magia(matriz,(fil-1,col),'O')
elif fil==3:
	matriz=magia(matriz,(fil,col),'E')
	matriz=magia(matriz,(fil,col),'O')
	matriz=magia(matriz,(fil-1,col),'E')
	matriz=magia(matriz,(fil-1,col),'O')
	matriz=magia(matriz,(fil-2,col),'E')
	matriz=magia(matriz,(fil-2,col),'O')
