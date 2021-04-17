'''
name = input("Введите имя: ")
print ("Меня зовут", name)
age = int(input("Введите возраст: "))
print( "Мне", age, "лет")
'''

def sec_to_hours(seconds):
    a=str(seconds//3600)
    b=str((seconds%3600)//60)
    c=str((seconds%3600)%60)
    print(f"{a} hours {b} mins {c} seconds")
print(sec_to_hours(2200))


a = int(input("Ведите число: "))
n = int('%s' % a)
nn = int ('%s%s' % (a, a))
nnn = int ('%s%s%s' % (a, a, a))
print (f"{n} + {nn} + {nnn}")
print (n + nn + nnn)

n = int(input("Введите число: "))
max = n % 10
while n >= 1:
    n = n // 10
    if n % 10 > max:
        max = n % 10
    if n > 9:
        continue
    else:
        print("Максимальное цифра в числе ", max)
        break


a = int(input("Введите результаты пробежки первого дня в км "))
b = int(input("Введите нужный результат в км "))
result_days = 1
result_km = a
while result_km < b:
        a = a + 0.1 * a
        result_days += 1
        result_km = result_km + a
print(f"Вы достигнете требуемых показателей на %.d день" % result_days)

