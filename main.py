from numpy import *
matriz=zeros(5,6)
for i in range(5):
        for j in range(6):
                matriz[i,j]=9
evitar=int(raw_input("Ingrese casilla para evitar:"))
if evitar<5:
        matriz[1,evitar]=6
elif evitar<9:
        matriz[2,evitar-4]=6
else:
        matriz[3,evitar-8]=6
ganar=raw_input("Ingrese casilla a la cual desea llegar:")
if ganar<5:
        matriz[1,ganar]=7
elif evitar<9:
        matriz[2,ganar-4]=7
else:
        matriz[3,ganar-8]=7
perder=raw_input("Ingrese casilla no accesible:")
if perder<5:
        matriz[1,perder]=8
elif perder<9:
        matriz[2,perder-4]=8
else:
        matriz[3,perder-8]=8
inicio=raw_input("Ingrese casilla de inicio:")
if inicio<5:
        matriz[1,inicio]=5
elif inicio<9:
        matriz[2,inicio-4]=5
else:
        matriz[3,inicio-8]=5
print matriz
