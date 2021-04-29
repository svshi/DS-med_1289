my_list = [1, 4, 7, 7, 4, 2, 2, 3, 2, 8, 10, 8, 5]
new_list = [el for el in my_list if my_list.count(el) == 1]
print(new_list)
