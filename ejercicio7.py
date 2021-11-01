while True:
    
    valores=input("")
    (X,M)=valores.split(" ")
    X=int(X)
    M=int(M)

    if (X==0) and M==0:
        break
    else:
        E=X*M

    print(E)