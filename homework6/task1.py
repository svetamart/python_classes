# Напишите программу вычисления арифметического выражения заданного строкой. 
# Используйте операции +,-,/,*. приоритет операций стандартный.

#  Пример:
#  2+2 => 4;
#  1+2*3 => 7;
#  1-2*3 => -5;

# Добавьте возможность использования скобок, меняющих приоритет операций.
#  Пример:
#  1+2*3 => 7;
#  (1+2)*3 => 9;



expression = input('Введите арифметическое выражение: ')

def parse(expression):
    num = ''
    exp = []
    for char in expression:
        if char.isdigit() or char == '.':
            num += char
        elif char == ' ':
            continue
        else:
            exp.append(float(num))
            num = ''
        if char in '/+-*':
                exp.append(char)
    if num:
            exp.append(float(num))
    return exp

# ОНО НЕ РАБОТАЕТ НАДО ПЕРЕДЕЛАТЬ

def calculator(exp):
    for i in range(len(exp)):
        if exp[i] == '/':
            if exp[i + 1] == 0:
                print('Деление на ноль')
                exit()
            exp[i] = exp[i - 1] / exp[i + 1]
        if exp[i] == '*':
            exp[i] = exp[i - 1] * exp[i + 1]
        if exp[i] == '+':
            exp[i] = exp[i - 1] + exp[i + 1]
        if exp[i] == '-':
            exp[i] = exp[i - 1] - exp[i + 1]
    return exp


print(parse(expression))
print(calculator(parse(expression)))