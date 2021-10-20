import numpy as np
def sinh():
    while True:
        i = k
        while i>0 and a[i] == n+i-k : i-=1
        if i>0 :
            a[i]+=1
            for j in range(i+1,k+1):
                a[j] = a[j-1] + 1
            print(*a[1:],sep="",end=" ")
        else: break
t = 2
while t:
    n = int(input("Nhap N = "))
    k = int(input("Nhap K = "))
    a = np.zeros(k+1,dtype=int)
    for i in range(1,k+1):
        a[i] = int(input())
    print(*a[1:],sep="",end=" ")
    sinh()
    print()
    t-=1