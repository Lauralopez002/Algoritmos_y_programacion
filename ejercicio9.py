alcohol=0
Gasolina=0
Diesel=0
n=0
while True:
    numero=int(input())
    if(n==1):
        alcohol+=1
    if(n==2):
        Gasolina+=1
    if(n==3):
        Diesel+=1
    if(n==4):
        break

print(f'Alcool: {alcohol}')
print(f'Gasolina: {Gasolina}')
print(f'Diesel: {Diesel}')
print('MUITO OBRIGADO')