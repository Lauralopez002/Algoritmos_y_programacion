N = int(input("Digite el valor de N: "))
K = int(input("Digite el valor de K: "))

while K >= N:
    N = int(input("Digite el valor de N: "))
    K = int(input("Digite el valor de K: "))
    print("Tenga en cuenta que K < N")


    
dif = N - K + 1
for i in range (dif):
    print(N) # 
    N = N - 1