str = "quangkhai-cn01-ptitita"
mylist = list(str)
set_list = set(x for x in mylist if mylist.count(x) > 2)
print(set_list)

mylist = list(map(lambda x : x**2,[1,2,3,4,5,6,7]))
print(mylist)

list_fiter = list(filter(lambda x: x>20,mylist)) #tim gia tri
print(list_fiter)