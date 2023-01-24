# Ex_4. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных. 
# Входные и выходные данные хранятся в отдельных текстовых файлах.

# b) Восстановление

# Создание списка их строк в файле
x = []
data = open('Ex_04_a_encode.txt', 'r')
for i in data:
    x.append(i.rstrip())
data.close()

# Функция RLE восстановления строки'
def decode(string):
    list1 = []
    temp_string = ''
    temp_num = ''
    for i in range(len(string)):
        if string[i].isdigit() == True:
            temp_num += str(string[i])
        else:
            temp_string += string[i]
            list1.append(int(temp_num) * temp_string)
            temp_string = ''
            temp_num = ''
    return "".join(list1)

# Функция записи сжатых элементов в файл построчно 
def write_in_file():
    data = open('Ex_04_b_decode.txt', 'w')
    for i in range(len(x)):      
        x[i] = decode(x[i])
        if i < len(x) - 1:
            data.writelines(x[i]+'\n')
        else:
            data.writelines(x[i])            
    data.close()

write_in_file()

print("Готово")