from random import *

board = []  # поле

for i in range(0, 4, 1):
    board.append(["O"] * 4)

ship = []

for i in range(0, 3, 1):
    ship_row = randint(0, len(board) - 1)  # генерация по столбику
    ship_col = randint(0, len(board[0]) - 1)  # генерация по строке
    ship.append([ship_row, ship_col])  # добавление кораблей

print('1)Легкий: 12 попыток')
print('2)Средний: 8 попыток')
print('3)Сложный: 4 попытки')
print('4)Невозможный: 2 попытки')

# Уровень сложности
level = int(input('Выбери уровень сложности:'))
w = 10
if level == 1:
    w = 12
elif level == 2:
    w = 8
elif level == 3:
    w = 4
elif level == 4:
    w = 2

print("Начнем игру в Морской бой!")

for x in board:
print(('|').join(x))

for turn in range(0, w, 1):
    guess_row = int(input("Строка 0-3:"))  # ввод столба
    guess_col = int(input("Столбец 0-3:"))  # ввод столба

hit = 0
for i in range(0, len(ship), 1):
    if ship[1] == [guess_row, guess_col]:
        hit = 1
        del ship[i]
board[guess_row][guess_col] = 's'
break

if 0 < hit:
    print('Вы выбили корабль')
if len(ship) == 0:
    print('Вы победили')

else:
    if (guess_row < 0 or guess_row > len(board)) or (guess_row < 0 or guess_col > len(board)):
        print('Эти координаты не в нашей компетенции')
    elif board[guess_row][guess_col] == 'X':
        print('Ты что дурак? Перезарядка...')
    else:
        print('Мимо!')
    board[guess_row][guess_col] = 'X'

for x in board:
    print((' ').join(x))

if turn == w - 1:
    print("Игра окончена! Я уплываю в закат!")
break