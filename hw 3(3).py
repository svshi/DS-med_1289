def my_func():
    arg1 = int(input('Enter first argument: '))
    arg2 = int(input('Enter second argument: '))
    arg3 = int(input('Enter third argument: '))
    if arg1 >= arg3 and arg2 >= arg3:
        return arg1 + arg2
    elif arg1 > arg2 and arg2 < arg3:
        return arg1 + arg3
    else:
        return arg2 + arg3


result = my_func()
print(result)
