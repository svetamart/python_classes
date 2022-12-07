import tkinter as tk
from tkinter import *
from tkinter import messagebox

window = Tk()
window.title('Tic-tac-toe')

window.geometry('360x390')
window.resizable(False, False)
window['background'] = 'alice blue'

messagebox.showinfo(f'Добро пожаловать!',
'''Добро пожаловать в игру "Крестики-нолики"! \n 
Первый ход делает игрок, который играет крестиками (Х). Передача хода от игрока к игроку происходит автоматически.
Чтобы сделать ход, просто щелкни на клетку поля левой кнопкой мыши.
Чтобы начать новую игру, нажми на кнопку "Новая игра".''')

game_run = True
buttons = []

player1 = 'X'
player2 = 'O'
count = 1
turns = 0

players = [player1, player2]
current_player = players[count]


def new_game():
    global turns
    turns = 0
    for row in range(3):
        for col in range(3):
            buttons[row][col]['text'] = ' '
            buttons[row][col]['background'] = 'alice blue'
    global game_run
    game_run = True


for row in range(3):
    line = []
    for col in range(3):
        button = Button(text=' ', width=5, height=2, font=('Courier', 28, 'bold'),
                        background='alice blue', command=lambda row=row, col=col: click(row, col))
        button.grid(row=row, column=col)
        line.append(button)
    buttons.append(line)
new_button = Button(window, text='Новая игра', font=('Courier', 20, 'bold'), background='alice blue', command=new_game)
new_button.grid(row=3, column=0, columnspan=3, rowspan=3)


def click(row, col):
    global turns
    if game_run and buttons[row][col]['text'] == ' ':
        buttons[row][col]['text'] = current_player
        turns += 1
        check_win(current_player)
        check_draw()
        player_change()


def player_change():
    global count, current_player
    count = not count
    current_player = players[count]


def check_draw():
    if turns == 9:
        messagebox.showinfo(f'Результат', 'Кажется, у нас ничья. Давайте сыграем еще раз!')


def check_win(name):
    for n in range(3):
        check_line(buttons[n][0], buttons[n][1], buttons[n][2], name)
        check_line(buttons[0][n], buttons[1][n], buttons[2][n], name)
    check_line(buttons[0][0], buttons[1][1], buttons[2][2], name)
    check_line(buttons[2][0], buttons[1][1], buttons[0][2], name)


def check_line(a1, a2, a3, name):
    if a1['text'] == name and a2['text'] == name and a3['text'] == name:
        a1['background'] = a2['background'] = a3['background'] = 'light coral'
        messagebox.showinfo(f'Результат', 'Побеждает Игрок ' + current_player + '! Поздравляем!')
        global turns
        turns = 0
        global game_run
        game_run = False


window.mainloop()
