# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.

# list = 45, 20, 4, 92, 10, 5, 79, 39, 63, 67, 2, 52, 83, 59, 18, 41, 11, 22, 90, 3
# product = 1


# for i in array:
#     for k in list:
#         while list[k] <= len(array):           # здесь все ломается :((
#             product *= array[list[k]]

# print(product)

n = int(input('Введите положительное число N '))
list2 = []
for i in range(-n, n + 1):
    list2.append(i)
print(list2)

path = 'file.txt' 
data = open(path, 'r') 
list1 = []
for line in data:
    if int(line) < len(list2):
        list1.append(list2[int(line)]) 

product = 1
for i in list1:
    product *= i
print(product)




