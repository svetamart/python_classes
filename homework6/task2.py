# Дана последовательность чисел. 
# Получить список уникальных элементов заданной последовательности, 
# список повторяемых и убрать дубликаты из заданной последовательности.

# Пример:
# [1, 2, 3, 5, 1, 5, 3, 10] => [2, 10] и  [1, 3, 5] и [1, 2, 5, 3, 10]


array = [1, 8, 2, 3, 5, 1, 5, 3, 10, 10, 16, 28, 3]
print(f'Исходный список: {array}')

unique = [i for i in array if array.count(i) == 1]

duplicate = []
[duplicate.append(i) for i in array if array.count(i) > 1 and i not in duplicate]

new_array = []
[new_array.append(i) for i in array if i not in new_array]
# new_array = list(set(array)) 

print(f'Уникальные элементы: {unique}')
print(f'Дубликаты: {duplicate}')
print(f'Список без дубликатов: {new_array}')
