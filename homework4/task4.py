# Задана натуральная степень k. 
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# k=2 => 2x^2 + 4x + 5 = 0 или x^2 + 5 = 0 или 10x^2 = 0

import random

k = int(input('Введите натуральную степень k: '))

coefficients = []
for i in range(0, 101):
    coefficients.append(i)

pol = []
for i in range(k, 1, -1):
    a = random.choice(coefficients)
    pol.append(f' {a}x^{i} ')

a = random.choice(coefficients)
pol.append(f' {a}x ')

a = random.choice(coefficients)
if a > 0:
    pol.append(f' {a} ')

result = '+'.join(pol) + '= 0'

if ' 1x' in result:
    result = result.replace(' 1x', ' x')
print(result)

# if ' 0x' in result:
#     result = result.split(' ')
#     print(result)
#     for i in result:
#         if '0x' in i:
#             result.remove(i)   
# print(result)  ------ в результирующем списке остаются плюсы, которые были между удаленными элементами

# with open('Polynomial.txt', 'w') as data:
#     data.write(result)