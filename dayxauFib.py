import numpy as np
def fib(n,k):
    if n == 1: return 'A'
    if n == 2: return 'B'
    if k <= F[n-2] : return fib(n-2,k)
    else: return fib(n-1 , k - F[n-2])
F = np.zeros(93)
F[1] = 1
for i in range(2,93):
    F[i] = F[i-1] + F[i-2]
print(type(F[6]))
t = 2
while t:
    N = int(input("Nhap N = "))
    K = int(input("Nhap K = "))
    c = fib(N,K)
    print(c)
    t-=1