t = int(input("Nhap so bo test : "))
while t :
    tu = int(input("Tu = "))
    mau = int(input("Mau = "))
    while True:
        if mau % tu == 0:
            print("1 /",mau//tu)
            break
        else :
            res = mau//tu + 1
            print("1 /",res,end=" + ")
            tu = tu*res - mau
            mau = mau * res
    t-=1