def taphop(i,k,sum):
    global dem
    if sum == S and i == K : dem+=1
    elif sum < S and i == K :return
    else:
        for j in range(k,N+1):
            tong = sum + j
            if tong > S : break
            if tong <= S :
                taphop(i+1,j+1,tong)
while True:
    N = int(input("Nhap N = "))
    K = int(input("Nhap K = "))
    S = int(input("Nhap S = "))
    if N == 0 and K == 0 and S == 0 :
        break
    dem = 0
    taphop(0,1,0)
    print(dem)

