t=4
while t:
    s = input("Nhap Xau : ")
    dem = 0
    mylist =[]
    for i in range(0,len(s)):
        if s[i] == '(' : mylist.append(s[i])
        else :
            if len(mylist) > 0 : mylist.pop()
            else :
                dem += 1
                mylist.append('(')
    print(dem+len(mylist)//2)
    t-=1