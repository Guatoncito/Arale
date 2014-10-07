def directo(gana, matriz):
	x,y = gana
	for i in range(6):
		matriz[0, i] = "M"
		matriz[4, i] = "M"
	for i in range(3):
		matriz[i+1, 0] = "M"
		matriz[i+1, 6] = "M"
	return matriz
def magia(matriz,tupla,direc):
	fil,col=tupla
	nada=True
	habn=False
	habs=False
	habe=False
	habo=False
	if matriz[fil+1,col]=='B':
		matriz[fil+1,col]='N'
		nada=False
		habn=True
	if matriz[fil-1,col]=='B':
		matriz[fil-1,col]='S'
		nada=False
		habs=True
	if matriz[fil,col+1]='B':
		matriz[fil,col+1]='O'
		nada=False
		habo=True
	if matriz[fil,col-1]=='B':
		matriz[fil,col-1]='E'
		nada=False
		habe=True
	if nada:
		return matriz
	if direc=='E' and habe:
		return magia(matriz,(fil,col+1),'E')
	if direc=='N' and habn:
		return magia(matriz,(fil-1,col),'N')
	if direc=='O' and habo:
		return magia(matriz,(fil,col-1),'O')
	if direc=='S' and habs:
		return magia(matriz,(fil+1,col),'S')

