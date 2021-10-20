t=3
while t:
    s = input("Nhap Xau : ")
    kq = 0
    mylist =[-1]
    for i in range(0,len(s)):
        if s[i] == '(' : mylist.append(i)
        else :
            mylist.pop()
            if len(mylist) > 0 :kq = max(kq,i-mylist[-1])
            else : mylist.append(i)
    print(kq)
    t-=1