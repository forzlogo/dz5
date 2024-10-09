from random import randint
list_ = []
for i in range(1,10):
    a = randint(0,10)
    list_.append(a)
    list_.sort()
print(list_[-1:])
