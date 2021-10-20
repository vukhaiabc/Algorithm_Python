t = int(input())
while t:
    n = int(input())
    mylist = ["9"]
    while True:
        s = mylist[0]
        mylist.pop(0)
        if int(s) % n == 0:
            print(s)
            break
        mylist.append(s+'0')
        mylist.append(s+'9')
    t-=1

