# Ex_4. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных. 
# Входные и выходные данные хранятся в отдельных текстовых файлах.

# a) Сжатие

# Создание списка их строк в файле
x = []
data = open('Ex_04_a_decode.txt', 'r')
for i in data:
    x.append(i.rstrip())
data.close()

# Функция RLE сжатия строки'
def encode(string):
    temp_string = ''
    if len(string) > 0:                # Проверка, что строка не пустая
        temp_char = string[0] 
        count = 0
        for i in range(len(string)):        
            if string[i] == temp_char:
                count += 1
            else:
                temp_string += str(count) + temp_char
                temp_char = string[i]
                count = 1
            if i == len(string) - 1:   # Вывод, если в строке 1 вид символа
                temp_string += str(count) + temp_char
        return temp_string
    else:                           # Вывод, если строка пустая
        return temp_string

# Функция записи сжатых элементов в файл построчно 
def write_in_file():
    data = open('Ex_04_a_encode.txt', 'w')
    for i in range(len(x)):      
        x[i] = encode(x[i])
        if i < len(x) - 1:
            data.writelines(x[i]+'\n')
        else:
            data.writelines(x[i])            
    data.close()

write_in_file()

print("Готово")