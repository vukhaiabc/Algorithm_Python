n = int(input("Nhap n : "))
lst = [0]*n
print(*lst,sep="",end=" ")
i = n-1
while i>=0:
    if lst[i] == 0 :
        lst[i] = 1
        for j in range(i+1,n):
            lst[j] = 0
        print(*lst,sep="",end=" ")
        i=n
    i-=1
