a = float(input("Введите результат пробежки в первый день в км: "))
b = float(input("Введите общий желаемый результат пробежки в км: "))
day = 1
result_km = a
while result_km < b:
    a = a + 0.1
    day += 1
    result_km = result_km + a
    print("На", day, "день спортсмен пробежал", result_km, "км.")
if result_km >= b:
    print ("На", day,"день спортсмен достиг результата", result_km, "км. Ура!" )
