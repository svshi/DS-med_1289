# ------------------------------------1-----------------------------
# Создать программно файл в текстовом формате, записать
# в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

my_file_1 = open('new.txt', 'w')
line = input('Введите текст \n')
while line:
    my_file_1.writelines(line)
    line = input('Введите текст \n')
    if not line:
        break

my_file_1.close()
my_func = open('new.txt', 'r')
content = my_func.readlines()
print(content)
my_func.close()


# ------------------------------------2-----------------------------
# Создать текстовый файл (не программно), сохранить
# в нем несколько строк, выполнить подсчет количества строк,
# количества слов в каждой строке.



my_file = open('test.txt', 'r')
content = my_file.read()
print(f'Содержимое файла: \n {content}')
my_file = open('test.txt', 'r')
content = my_file.readlines()
print(f'Количество строк в файле - {len(content)}')
my_file = open('test.txt', 'r')
content = my_file.readlines()
for i in range(len(content)):
    print(f'Окличество символов {i + 1} - ой строки {len(content[i])}')
my_file = open('test.txt', 'r')
content = my_file.read()
content = content.split()
print(f'Общее количество слов - {len(content)}')
my_file.close()


# ------------------------------------4-----------------------------
# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

rus = {'One': 'Odin', 'Two': 'Dva', 'Three': 'Tree', 'Four': 'Chetyre'}
new_file = []
with open('file.txt', 'r') as file_obj:
    for i in file_obj:
        i = i.split(' ', 1)
        new_file.append(rus[i[0]] + '  ' + i[1])
    print(new_file)

with open('file_2.txt', 'w') as file_obj_2:
    file_obj_2.writelines(new_file)

# ------------------------------------5-----------------------------
# Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.


def summary():
    try:
        with open('file_1', 'w+') as file_obj:
            line = input('Введите цифры через пробел: \n')
            file_obj.writelines(line)
            my_numb = line.split()

            print(sum(map(int, my_numb)))
    except IOError:
        print('Ошибка в файле')
    except ValueError:
        print('Неправильно набран номер. Ошибка ввода-вывода')


summary()




