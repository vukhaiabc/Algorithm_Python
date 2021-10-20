t=4
while t:
    s = input("Nhap Day : ")
    n = len(s)
    mylist = []
    for i in range(0,n+1):
        if  i == n or s[i] == 'I' :
            print(i+1,end="")
            while len(mylist) > 0:
                print(mylist[-1],end="")
                mylist.pop()
        else:mylist.append(i+1)
    print()
    t-=1