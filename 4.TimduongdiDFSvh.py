import numpy as np
n = int(input("so dinh : "))
m = int(input("so canh : "))
start = int(input("start : "))
end = int(input("end : "))
a = np.zeros((n+1,n+1),dtype=int)
chuaxet = np.ones(n+1,dtype=bool) #true
truoc = np.zeros(n+1,dtype=int)
for i in range(0,m):
    x = int(input())
    y = int(input())
    a[x][y] = 1
    a[y][x] = 1
def DFS(u):
    chuaxet[u] = False
    for v in range(1,n+1):
        if chuaxet[v] and a[u][v] :
            truoc[v] = u
            DFS(v)
def duongdi(start,end):
    mylist =[end]
    while mylist[-1] != start :
        dinh = mylist[-1]
        mylist.append(truoc[dinh])
    print(*list(reversed(mylist)))
DFS(start)
if chuaxet[end] : print(-1)
else: duongdi(start,end)