# Вычислить число c заданной точностью d
# Пример:
# при d = 0.001, π = 3.142 10^(-1) ≤ d ≤10^(-10)

import random
from decimal import Decimal

d = random.uniform(10 ** (-10), 10 ** (-1))
d = round(d, random.randint(1, 12))
print(d)

number = Decimal(input('Введите вещественное число: '))
number = number.quantize(Decimal(str(d)))          # почему-то без перевода в строку не работает, хотя по идее должно
print(number)