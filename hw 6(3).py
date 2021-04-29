# # вариант 1
# def my_func(*args):
#     word = input("Input words ")
#     print(word.title())
#     return my_func()
#
#
# print(my_func())
#

# вариант 2

def my_func(a):
    separate_word = a.split(' ')
    total = []
    for i in separate_word:
        string_element = str(i)
        first_letter = string_element[:1].upper()
        word = first_letter + string_element[1:]
        total.append(word)
    return total


print(my_func("hello world"))

