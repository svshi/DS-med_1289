def my_func(name, surname, year, city, email, phone):
    name = input('enter name: ')
    surname = input('enter surname: ')
    year = int(input('enter year: '))
    city = input('enter city: ')
    email = input('enter email: ')
    phone = input('input phone: ')
    return name, surname, year, city, email, phone


print(my_func(surname='', name='', year='', city='', email='', phone=''))
