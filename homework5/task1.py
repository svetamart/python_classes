# Напишите программу, удаляющую из текста все слова, в которых присутствуют все буквы "абв".

text = '''Дурсли содрогались абвабв при одной мысли о том, 
что скажут соседи, ааавабв если на Тисовую улицу пожалуют Поттеры. 
Дурсли знали, что у Поттеров абвабдлФВЫТабв тоже есть маленький сын, 
но они никогда его не автобус видели. И они АВБ категорически не хотели, 
чтобы их Дадли общался с ребенком таких ышыфлвоабв родителей.'''

new = list(filter(lambda i: not ('а' in i.lower() and 'б' in i.lower() and 'в' in i.lower()), text.split(' ')))
print(' '.join(new))

print()

# ВАРИАНТ 2

new_text = []
for i in text.split(' '):
    tmp = i.lower()
    if not ('а' in tmp and 'б' in tmp and 'в' in tmp):
        new_text.append(i)
print(' '.join(new_text))

print()

# ВАРИАНТ 3

print(*filter(lambda i: not all(True if char in i.lower() else False for char in 'абв'), text.split(' ')), sep=' ')