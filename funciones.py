def directo(gana, matriz):
	x,y = gana
	for i in range(6):
		matriz[0, i] = "M"
		matriz[4, i] = "M"
	for i in range(3):
		matriz[i+1, 0] = "M"
		matriz[i+1, 6] = "M"
	return matriz

