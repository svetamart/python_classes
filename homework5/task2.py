# Создайте программу для игры с конфетами человек против человека.

# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

import random

player1 = input('Введите имя первого игрока: ')
player2 = input('Введите имя второго игрока: ')
players = [player1, player2]
candy = int(input('Сколько конфет лежит на столе? '))

msg = ['сколько конфет возьмете?', 'пора брать конфеты!', 'ваш ход!']

turn = random.randint(0, 1)
if turn:
    count = 0
else:
    count = 1
print(f'Первый ход делает {players[count]}')


def game(candy, players, count, msg):
    while candy > 0:
        print(f'{players[count]}, {random.choice(msg)}')
        move = int(input())
        if move > candy or move > 28:
            print(f'Многовато конфет вы взяли, {players[count]}. Всего у нас осталось {candy}. Давайте брать не больше 28 за раз?')
        elif move == 0:
            print(f'Хмм, что-то тут не так. Вы не взяли ни одной конфеты, {players[count]}! Так не пойдет, давайте-ка еще раз.')
        else:
            candy -= move
            print(f'{players[count]} взял {move} конфет. На столе осталось {candy}.')
            if candy != 0:
                count = not count
    return players[count]

winner = game(candy, players, count, msg)
print(f'{winner} делает последний ход и забирает себе все конфеты своего оппонента! {winner} победил!')