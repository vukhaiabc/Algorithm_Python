t = int(input())
while t:
    n = int(input())
    mylist = ["1"]
    dem = 0
    while dem != n:
        s = mylist[0]
        mylist.pop(0)
        dem+=1
        print(s,end=" ")
        mylist.append(s+"0")
        mylist.append(s+"1")
    print()
    t-=1