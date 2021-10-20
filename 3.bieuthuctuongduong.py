t = 2
while t:
    s = input("Nhap chuoi : ")
    str = list(s)
    n = len(s)
    mylist = []
    for i in range(0,n):
        if str[i] == '(' :
            mylist.append(i)
        elif str[i] == ')':
            top = mylist[-1]
            if str[top - 1] == '-':
                for j in range(top+1,i):
                    if str[j] == '-' : str[j] = '+'
                    elif str[j] == '+' : str[j] = '-'
            mylist.pop()
    for i in str:
        if i!='(' and i!=')':
            print(i,end="")
    print()
    t-=1