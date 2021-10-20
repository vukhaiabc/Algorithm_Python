def uuTien(c):
    if c == '+' or c == '-' : return 1
    if c == '*' or c == '/' or c == '%': return 2
    if c == '^': return 3
    return 0
def trungSanghau():
    s = input("Nhap chuoi : ")
    n = len(s)
    list=[]
    str = ""
    for i in range(0,n):
        c = s[i]
        if c.isalpha():str+=c
        elif c == '(' : list.append(c)
        elif c == ')' :
            while len(list) > 0 and list[-1] != '(':
                str += list[-1]
                list.pop()
            list.pop()
        else :
            while(len(list) > 0 and uuTien(c) <= uuTien(list[-1])):
                str+=list[-1]
                list.pop()
            list.append(c)
    while len(list) > 0 :
        str+= list[-1]
        list.pop()
    print(str)
trungSanghau()