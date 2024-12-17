# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# See PyCharm help at https://www.jetbrains.com/help/pycharm/

#1st program
"""Выведите на экран(в консоль) результат: возведение числа 9 в степень 0.5, после умножение на 5.
Предполагаемый результат: 15.0"""
if __name__ == '__main__':
    a = 9
    b = 0.5
    c = 5
    print("1st program:", a ** b * c)

#2nd program
"""Убедитесь в том что 9.99 больше 9.98 и 1000 не равно 1000.1 одновременно, выведете результат на экран(в консоль)
 Предполагаемый результат: True"""
if __name__ == '__main__':
    a = 9.99
    b = 9.98
    c = 1000
    d = 1000.1
    print("2nd program:",a > b and c != d)

 #3d program
"""Выведите на экран (в консоль) 2 умноженное на 2 плюс 2 без приоритета.
Выведите на экран (в консоль) 2 умноженное на 2 плюс 2 с приоритетом для сложения.
Выведите на экран (в консоль) результат сравнения этих двух выражений.
Предполагаемый результат (с использованием ==): False"""
if __name__ == '__main__':
    a = 2 * 2 + 2
    b = 2 * (2 + 2)
    print("3d program:")
    print(a)
    print(b)
    print(a == b)

#4th program
"""Дана строка '123.456'.
Вывести на экран первую цифру после запятой - 4."""
if __name__ == '__main__':
    a = '123.456'
    b = (float(a) * 10) % 10
    print("4th program:", int(b))