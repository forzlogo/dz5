from random import randint
list_ = []
for i in range(1,11):
    a = randint(1,10)
    list_.append(a)
print(f'был - {list_}')
list_.clear()
print(f'стал - {list_}')
