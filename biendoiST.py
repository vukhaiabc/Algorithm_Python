t= 3
while t:
    S = int(input("Nhap S : "))
    T = int(input("Nhap T : "))
    mylist = [(S,0)]
    sett = {S}
    while len(mylist) > 0:
        val = mylist[0][0]  #vitri dau tien
        dem = mylist[0][1]
        mylist.pop(0)
        if val == T :
            print(dem)
            break
        if 2*val == T or val - 1 == T :
            print(dem+1)
            break
        if 2*val not in sett and val < T:
            mylist.append((2*val,dem+1))
        if val-1 not in sett and val -1 > 0:
            mylist.append((val-1,dem+1))
    t-=1
