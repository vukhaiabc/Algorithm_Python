import numpy as np
k = int(input("Nhap k :"))
s = input("Nhap chuoi so :")
n = len(s)
a=[]
for i in range(0,len(s)):
    a.append(int(s[i]))
i = 0
while i<n:
    max = a[n-1]
    vtmax = n-1
    for j in range(n-1,i,-1):
        if a[j] > max :
            max = a[j]
            vtmax = j
    if k>0 and a[i] < a[vtmax]:
        a[i],a[vtmax] = a[vtmax],a[i]
        k-=1
    i+=1
print(*a)