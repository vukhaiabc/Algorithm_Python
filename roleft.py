a = []
while True:
    n = int(input())
    a.append(n)
    if(len(a) == a[0]+2) : break

num = a[1]
my_arr = a[2:]
# 1,2,3,4,5 => 5,1,2,3,4 xoay 4 lan
while num:
    a = my_arr[0]
    my_arr.append(a)
    my_arr.pop(0)
    num-=1
print(my_arr)
