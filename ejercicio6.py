n1=int(input("digite el valor n1: "))
n2=int(input("digite el valor n2: "))
#caja negra
while True:
    if (n1>=n2):
        print(n1,"-",n2,"=",n1-n2)
        n1=n1-n2
    else:
        break