from random import randint
sum = 0
list_ = []
for i in range(1,10):
    a = randint(0,10)
    list_.append(a)
    list_.sort()
for j in list_:
    sum += j
print(sum)
