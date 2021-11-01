cont=97
suma=97

for i in range (97,1004):
    if (cont%2==0):
        cont=cont+1
        suma=suma+cont
    elif (cont%2!=0):
        cont=cont+1
        suma=suma+0
    print("el resultado es igual a: ", suma)