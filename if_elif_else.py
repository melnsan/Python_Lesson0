a = input('Введите 1-е число: ')
b = input('Введите 2-е число: ')
c = input('Введите 3-е число: ')

if a == b and b == c:
    print('Вы ввели 3 одинаковых числа')
elif a == b or b == c or a == c:
    print('Вы ввели 2 одинаковых числа')
else:
    print('Вы ввели 0 одинаковых чисел')