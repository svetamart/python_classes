# Задайте последовательность чисел. 
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

import random
n = int(input('Введите длину списка: '))
list1 = []
for i in range(n):
    list1.append(random.randint(0, 8))
print(list1)

list2 = []
for i in range(len(list1) + 1):
    if list1.count(i) == 1:
        list2.append(i)
print(list2)