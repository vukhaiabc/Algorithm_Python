import numpy as np
n = int(input("Nhap n :"))
m = int(input("Nhap m :"))
a = np.zeros((10,10))
chuaxet = np.ones(10)
def DFS(u):
    chuaxet[u] = 0;
    print(u,end=" ")
    for v in range(1,n+1):
        if a[u][v] == 1 and chuaxet[v] == 1 :
            DFS(v)
for i in range(0,m):
    u = int(input())
    v = int(input())
    a[u][v]=1
    a[v][u]=1
DFS(5)