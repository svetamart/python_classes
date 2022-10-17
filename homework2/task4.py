# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.

n = int(input('Введите положительное число N '))

list = 45, 20, 4, 92, 10, 5, 79, 39, 63, 67, 2, 52, 83, 59, 18, 41, 11, 22, 90, 3
product = 1
array = [i for i in range(-n, n + 1)]
print(*array, sep=', ')

for i in array:
    for k in list:
        while list[k] <= len(array):           # здесь все ломается :((
            product *= array[list[k]]

print(product)
