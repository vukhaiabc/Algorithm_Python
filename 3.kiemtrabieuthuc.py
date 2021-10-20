import numpy as np
def check(s,m,n):
    chuaxet[m] = False
    chuaxet[n] = False
    for i in range(m+1,n):
        if chuaxet[i]:
            chuaxet[i] = False
            if s[i] == "+" or s[i] == '-' or s[i] == '*' or s[i] == '/' or s[i] == '^' :
                return True #bieu thuc dung
    return False
t=3
while t:
    s = input("Nhap Xau : ")
    mylist =[]
    chuaxet = np.ones(len(s),dtype=bool)
    Flag = True
    for i in range(0,len(s)):
        if s[i] == '(' : mylist.append(i)
        elif s[i] == ')' :
            top = mylist[-1]
            if(check(s,top,i) == False):
                Flag = False
                break
            mylist.pop()
    print("YES") if Flag==False else print("NO")
    t-=1