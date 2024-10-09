list = []
for i in range(1, 11):
    num = int(input("Введите четное число - "))
    if num % 2 == 0:
        list.append(num)
    else:
        print("Вводите только четные числа")
        break
print(list)
