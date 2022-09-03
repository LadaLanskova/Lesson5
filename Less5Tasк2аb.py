"""
2. Создайте программу для игры с конфетами человек против человека.
Условие задачи: На столе лежит 2021 конфета.
Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой.
За один ход можно забрать не более чем 28 конфет.
Все конфеты оппонента достаются сделавшему последний ход.
Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
a) Добавьте игру против бота
б) Подумайте, как наделить бота "интеллектом"
"""

# вариант человек против Бота/Умного бота
from random import randint

def input_dat(name):
    ok = False
    while not ok:
        x = input(f"{name}, введите количество конфет, которое возьмете от 1 до 28: ")
        if x.isdigit() and 1 <= int(x) <= 28:
            ok = True
        else:
            print(f"{name}, Вы ошиблись, введите число от 1 до 28:")
    return x

def bot_calc(value):
    if value > 57:
        k = randint(1, 28)
    else:
        k = value - 29
    return k


def p_print(name, k, counter, value):
    print(f"Ходил {name}, он взял {k} конфет, теперь у него {counter}. На столе осталось {value} конфет.\n")


print('Здравствуйте! Вас приветствует игра "Забери все конфеты!" \n'
            'Основные правила игры: \n'
            'На столе 2021 конфета, \n'
            'за один ход мы можем взять не более 28 конфет, \n'
            'Итак, начнём!\n')

player1 = input("Давайте познакомимся! Как Вас зовут?: ")
ok = False
while not ok:
    um = input("Вы хотите играть против обычного бота (нажмите 0) или против бота с интеллектом (нажмите 1)?")
    if um.isdigit() and 0 <= int(um) <= 1:
        ok = True
    else:
        print(f"{player1}, Вы ошиблись, введите 0 или 1:")
if int(um):
    player2 = "Умный бот"
    print(f"Приятно познакомиться, {player1}! Вы играете против Умного бота")
else:
    player2 = "Бот"
    print(f"Приятно познакомиться, {player1}! Вы играете против Бота")
value = 2021
print()
print(f"На столе {value} конфета. Поехали!\n")


flag = randint(0, 1)
if flag:
    print(f"Первым ходит {player1}")
else:
    print(f"Первым ходит {player2}")

counter1 = 0
counter2 = 0

while value > 28:
    if flag:
        k = int(input_dat(player1))
        counter1 += k
        value -= k
        flag = False
        p_print(player1, k, counter1, value)
    else:
        if not int(um):
            k = randint(1, 28)
        else:
            k = bot_calc(value)
        counter2 += k
        value -= k
        flag = True
        p_print(player2, k, counter2, value)

if flag:
    print(f"Игра закончена! Поздравляем, {player1}, Вы выиграли!")
else:
    print(f"Игра закончена! {player1}, к сожалению, выиграл {player2}")