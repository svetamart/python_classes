# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
#  Пример:

# 45 -> 101101
# 3 -> 11
# 2 -> 10


n = int(input('Введите число: '))
temp = int(n)
result = ''
while temp:
    result = str(temp % 2) + result
    temp //= 2
print(f'{n} --> {result}')