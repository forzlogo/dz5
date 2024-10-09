from random import randint
list_ = []
for i in range(1,11):
    a = randint(0,10)
    list_.append(a)
    list_.sort()
    print(list_)
print(list_[-2:-1])
