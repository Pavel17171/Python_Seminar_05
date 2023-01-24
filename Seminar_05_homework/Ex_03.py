#Ex_3. Создайте программу для игры в ""Крестики-нолики"".

# Задаем условия
string1 = "-"                                                       # Горизонтальные разделительные линии
string2 = "| 1 | 2 | 3 || 4 | 5 | 6 || 7 | 8 | 9 |"                 # Заполнение строк доски
win = ("123", "456", "789", "147", "258", "369", "159", "357")      # Условия победы
x = ""                                                              # Запись ходов первого игрока
o = ""                                                              # Запись ходов второго игрока
player1 = "Первый"
player2 = "Второй"
flag = True

# Функция вывода доски
def Board():
    print(string1 * 13, string2[0:13], 
          string1 * 13, string2[13:26], 
          string1 * 13, string2[26:], 
          string1 * 13, sep = "\n")

# Функция хода игрока
def Step(player, list_step, symbol):
    number = int(input(f"Ходит {player} игрок: "))         # Ввод значения
    global string2                                        
    global x
    global o    
    if str(number) in string2:                            # Проверяем свободна ли ячейка
        string2 = string2.replace(str(number), symbol)    # Замена номера ячейки на доске на введеное значение
        if list_step == x:
            x += str(number)
            list1 = x
        else:
            o += str(number)
            list1 = o              
        Board()
        Check(list1)
    else:
        print("Эта клетка занята, попробуйте другую")
        Step(player, list_step, symbol)                   # Повтор функции

# Функция проверки победной комбинации
def Check(list_answer):
    for i in range(len(win)):
        count = 0
        global flag
        for j in range(len(win[i])):
            if win[i][j] in list_answer:
                count += 1
        if count == 3:
            flag = False
            break

# Функция запуска игры
def game():
    i = 0
    while flag == True or i < 10:
        if i % 2 == 0:
            player = player1
            list1 = x
            symbol = 'X'
        else:
            player = player2
            list1 = o
            symbol = 'O'   
        Step(player, list1, symbol)      
        if flag == False:
            print(f"{player} игрок победил")
            break
        i += 1
        if i == 9:
            print("Ничья")
            break

Board() # Первый запуск новой доски
game()  # Запуск игры
