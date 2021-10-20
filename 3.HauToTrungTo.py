t = 2
#  ABC++   ==> (A+(B+C))
while t:
    s = input("Nhap Chuoi : ")
    n = len(s)
    mylist = []
    for c in s:
        if c.isalpha() : mylist.append(c)
        else:
            s1 = mylist[-1]   # C
            mylist.pop()
            s2 = mylist[-1]   # B
            mylist.pop()
            str = '(' + s2 + c + s1 + ')'
            mylist.append(str)
    print(*mylist)
    t-=1