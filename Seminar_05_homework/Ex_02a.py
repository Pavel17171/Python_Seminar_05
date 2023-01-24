# Ex_2. а) Создайте программу для игры с конфетами человек против бота...

import random

# Условия
candy = int(input("Введите количество конфет: "))
max_candies = int(input("Сколько можно взять максимум конфет за 1 ход: "))
player1 = 0
robot = 0

# Жеребьевка первого хода
count = random.randint(1, 3)

# Функция ввода числа и проверка на сообветствие условиям
def Input_number():
    number = input()
    if number.isdigit() == True:
        number = int(number)
        if number > 0 and number <= max_candies:
            return number
        else:
            print("Введено некорректное значение")
            return Input_number()
    else:
        print("Введено некорректное значение")
        return Input_number()

# Функция расчета, сколько нужно взять конфет за ход для победы
def Recommendate():
    if (candy + robot) % (max_candies + 1) == 0:
        print(f"Player 1 (рекомендуется взять {max_candies + 1 - robot} конфет): ")
    else:
        if candy % (max_candies + 1) == 0:
            print(f"Player 1 (рекомендуется взять {max_candies } конфет): ")
        else:
            print(f"Player 1 (рекомендуется взять {candy % (max_candies + 1)} конфет): ")

# Ходы по очереди
while candy > 0:
    if count % 2 == 0:
        Recommendate()
        player1 = Input_number() 
        candy -= player1
        count += 1
        print(f"Player 1 взял {player1} конфет")
        print(f"Осталось {candy} конфет")
    else:
        print(f"Robot: ")        
        robot = random.randint(1, max_candies)
        candy -= robot
        count += 1
        print(f"Robot взял {robot} конфет")
        print(f"Осталось {candy} конфет")

# Вывод победителя
if count % 2 == 0:
    print("Robot - WIN")
else:
    print("Player 1 - WIN")    