# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

number = int(input('Введите натуральное число N: '))
n = number
i = 2
prime_factors = []
while i * i <= n:
    while n % i == 0:
        prime_factors.append(i)
        n //= i
    i += 1
if n > 1:
       prime_factors.append(n)

print(f'Простые множители числа {number}: {prime_factors}')