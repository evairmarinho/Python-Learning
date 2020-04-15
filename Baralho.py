naipes = ["Espadas","Copas","Ouros","Paus"]
simbolos = ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]
cartas=[' '],[' ']
k=0
l=0

for i in naipes:
    for j in simbolos:
       cartas[k][l]=i+" "+j
       print(cartas[k][l])
       l+1
k+1