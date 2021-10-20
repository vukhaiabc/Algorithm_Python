def Try(n,k):
    mid = pow(2,n-1)
    if k == mid : return n
    if k < mid :return Try(n-1,k)
    else : return Try(n-1,k-mid)
t = int(input("So bo test : "))
while t:
    N = int(input("Nhap N = "))
    K = int(input("Nhap K = "))
    print(Try(N,K))
    t-=1