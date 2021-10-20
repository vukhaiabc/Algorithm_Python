import numpy as np
n = int(input("so dinh : "))
m = int(input("so canh : "))
a = np.zeros((n+1,n+1),dtype=int)
chuaxet = np.ones(n+1,dtype=bool) #true
for i in range(0,m):
    x = int(input())
    y = int(input())
    a[x][y] = 1
    a[y][x] = 1
def DFS(u):
    chuaxet[u] = False
    for v in range(1,n+1):
        if chuaxet[v] and a[u][v] :
            DFS(v)
for i in range(1,n+1):
    chuaxet[i] = False
    if i == 1 : DFS(2)
    else: DFS(1)
    if True in chuaxet[1:n+1] :
        print(i,end=" ")
    chuaxet = np.ones(n+1,dtype=bool)