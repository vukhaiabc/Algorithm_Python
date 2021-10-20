import numpy as np
n = int(input("Nhap N = "))
chuaxet = np.ones(n+1,dtype=bool)
a = np.zeros(n,dtype=int)
def hoanvi(i):
    for j in range(1,n+1):
        if chuaxet[j]:
            chuaxet[j] = False
            a[i] = j
            if i == n-1 :
                print(*a,sep="",end=" ")
            else :hoanvi(i+1)
            chuaxet[j]= True
hoanvi(0)