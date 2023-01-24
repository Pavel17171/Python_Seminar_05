# Ex_2. b) Создайте программу для игры с конфетами человек против бота с интелектом...

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
def Smart_bot():
    if (candy + player1) % (max_candies + 1) == 0:
        return max_candies + 1 - player1
    else:
        if candy % (max_candies + 1) == 0:
            return max_candies
        else:
            return candy % (max_candies + 1)

# Ходы по очереди
while candy > 0:
    if count % 2 == 0:
        print("Player 1 ")         
        player1 = Input_number() 
        candy -= player1
        count += 1
        print(f"Player 1 взял {player1} конфет")
        print(f"Осталось {candy} конфет")
    else:
        print(f"Robot: ")        
        robot = Smart_bot()
        candy -= robot
        count += 1
        print(f"Robot взял {robot} конфет")
        print(f"Осталось {candy} конфет")

# Вывод победителя
if count % 2 == 0:
    print("Robot - WIN")
else:
    print("Player 1 - WIN")    