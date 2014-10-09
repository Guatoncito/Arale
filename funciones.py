def directo(matriz):
	for i in range(6):
		matriz[0, i] = "M"
		matriz[4, i] = "M"
	for i in range(3):
		matriz[i+1, 0] = "M"
		matriz[i+1, 5] = "M"
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
	if matriz[fil,col+1]=='B':
		matriz[fil,col+1]='O'
		nada=False
		habe=True
	if matriz[fil,col-1]=='B':
		matriz[fil,col-1]='E'
		nada=False
		habo=True
	if nada:
		return matriz
	if direc=='E' and habe:
		return magia(matriz,(fil,col+1),'E')
	elif direc=='E' and not habe:
		return matriz
	if direc=='N' and habn:
		return magia(matriz,(fil-1,col),'N')
	elif direc=='N' and not habn:
		return matriz
	if direc=='O' and habo:
		return magia(matriz,(fil,col-1),'O')
	elif direc=='O' and not habo:
		return matriz
	if direc=='S' and habs:
		return magia(matriz,(fil+1,col),'S')
	elif direc=='S' and not habs:
		return matriz

