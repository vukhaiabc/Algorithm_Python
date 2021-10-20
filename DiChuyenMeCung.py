import numpy as np
n=5
a = np.array([[1,0,0,0,0],[1,1,1,1,1],[1,1,0,0,1],[0,1,1,1,1],[0,0,0,1,1]])
lst=[]
dem = 0
def dichuyen(x,y,s):
    if x==n-1 and y==n-1 :
        lst.append(s)
    if x < n-1 and a[x+1,y]  : dichuyen(x+1,y,s+"D")
    if y < n-1 and a[x,y+1]  : dichuyen(x,y+1,s+"R")
dichuyen(0,0,"")
for item in lst:
    print(item,end=" ")