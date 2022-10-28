# Создайте программу для игры в ""Крестики-нолики"".


print('Добро пожаловать в игру "Крестики и нолики"!')
x = 'X'
o = 'O'

player1 = x
player2 = o
players = [player1, player2]

start = input('Игрок 1, Вы хотите сделать первый ход и играть крестиками? (да/нет) ').lower()

def check_answer(start):
    while start in ['да', 'нет']:
        return True
    else:
        print('Что-то пошло не так. Введите свой ответ еще раз.')
        return False        # не понимаю, как в случае ошибки остановить программу и заставить вернуться к ответу на вопрос

if check_answer(start):
    if start == 'да':
        print('Отлично! Игрок 1 играет крестиками!')
        count = 0
        current_player = players[count]
    else:
        print('Ладно, тогда Игрок 2 будет ходить первым и играть крестиками.')
        player1 = o  # почему-то Игрок 2 продолжает ходить ноликами, хотя я присвоила ему значение другой переменной
        player2 = x
        count = 1
        current_player = players[count]


def board(value): 
    print('\n') 
    print('\t     |     |') 
    print('\t  {}  |  {}  |  {}'.format(value[0], value[1], value[2])) 
    print('\t_____|_____|_____') 
  
    print('\t     |     |') 
    print('\t  {}  |  {}  |  {}'.format(value[3], value[4], value[5])) 
    print('\t_____|_____|_____') 
  
    print('\t     |     |') 
  
    print('\t  {}  |  {}  |  {}'.format(value[6], value[7], value[8])) 
    print('\t     |     |') 
    print('\n') 

value = [' ' for i in range(9)]

def tictactoe(value, current_player):
    valid = False
    while not valid:
        number = int(input(f'Игрок {current_player}, делайте свой ход: '))
        print('''Чтобы сделать ход, введите номер клетки,
куда хотите поставить свой Х или О.
            1 | 2 | 3
            ---------
            4 | 5 | 6
            ---------
            7 | 8 | 9''')
        try:
            number = int(number)
        except:
            print('Что-то пошло не так. Вы уверены, что ввели число?')
            continue
        if number >= 1 and number <= 9:
            if value[number - 1] != ' ':
                print('Эта клетка уже занята')
            else:
                value[number - 1] = current_player
                valid = True
        else:
            print('Клетки с таким номером на поле не существует. Попробуйте еще раз')        

def victory(value):
    combos = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for i in combos:
        if value[i[0]] == value[i[1]] == value[i[2]] != ' ':
            return True
    return False

def main(value, count, current_player, players):
    win = False
    while not win:
        board(value)
        tictactoe(value, current_player)
        victory(value)
        if victory(value):
            print(f'Побеждает Игрок {current_player}! Поздравляем!')
            win = True
            break
        if value.count(players[0]) + value.count(players[1]) == 9: 
            print('Кажется, у нас ничья. Сыграем еще раз?')
            break
        count = not count
        current_player = players[count]
    board(value)

main(value, count, current_player, players)