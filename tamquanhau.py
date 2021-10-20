import numpy as np
h = np.zeros(10,dtype=bool)
c = np.zeros(10,dtype=bool)
xuoi = np.zeros(20,dtype=bool)
nguoc = np.zeros(20,dtype=bool)
n = int(input("Nhap n :"))
dem = 0
def tamquanhau(i):
    global dem
    for j in range(1,n+1):
        if not(h[j]) and not(c[j]) and not(xuoi[i+j-1]) and not(nguoc[i-j+n]):
            h[j] = c[j] = xuoi[i+j-1] = nguoc[i-j+n] = True
            if(i==n): dem+=1
            else: tamquanhau(i+1)
            h[j] = c[j] = xuoi[i + j - 1] = nguoc[i - j + n] = False
tamquanhau(1)
print(dem)