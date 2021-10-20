import numpy as np
h = np.zeros(10,dtype=bool)
c = np.zeros(10,dtype=bool)
xuoi = np.zeros(20,dtype=bool)
nguoc = np.zeros(20,dtype=bool)
tong = 0
kq = 0
def tamquanhau(i):
    global tong,kq
    for j in range(1,9):
        if not(h[j]) and not(c[j]) and not(xuoi[i+j-1]) and not(nguoc[i-j+8]):
            tong += 8*(i-1) + j
            h[j] = c[j] = xuoi[i+j-1] = nguoc[i-j+8] = True
            if(i==8): kq = max(kq,tong)
            else: tamquanhau(i+1)
            tong -= 8 * (i - 1) + j
            h[j] = c[j] = xuoi[i + j - 1] = nguoc[i-j+8] = False
tamquanhau(1)
print(kq)