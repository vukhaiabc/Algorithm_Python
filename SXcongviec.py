import numpy as np
t = int(input())
while t:
    n = int(input())
    arr1 = np.zeros(n)
    arr2 = np.zeros(n)
    for i in range(0,n):
        arr1[i] = int(input())
    for i in range(0,n):
        arr2[i] = int(input())
    mylist = list(zip(arr1,arr2))
    resultlist = sorted(mylist,key=lambda x:x[1])
    i=1;j=0
    dem = 1
    while i<n :
        if resultlist[i][0] >= resultlist[j][1]:
            dem+=1
            j=i
        i+=1
    print(dem)
    i-=1