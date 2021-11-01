k=1
e=0
a=0

print()
while(e<=1000):
    e=((k**2)+1)/k
    k=k+1
    a=a+1
    if e>=1000:
        e=((k**2)+1)/k
        k=k+1
        a=a-1
        break
    
    print (a)