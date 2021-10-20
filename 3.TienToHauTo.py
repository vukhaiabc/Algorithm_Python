t = 2
# *+AB-CD  ==> AB+CD-*
while t:
    s = input("Nhap chuoi : ")
    n = len(s)
    mylist = []
    for i in range(n-1,-1,-1):
        c = s[i]
        if c.isalpha() : mylist.append(c)
        else :
            s1 = mylist[-1]
            mylist.pop()
            s2 = mylist[-1]
            mylist.pop()
            str = s1+s2+c
            mylist.append(str)
    print(*mylist)
    t-=1