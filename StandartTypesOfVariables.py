# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# See PyCharm help at https://www.jetbrains.com/help/pycharm/

#1st program
if __name__ == '__main__':
    a = 9
    b = 0.5
    c = 5
    print("1st program:", a ** b * c)

#2nd program
if __name__ == '__main__':
    a = 9.99
    b = 9.98
    c = 1000
    d = 1000.1
    print("2nd program:",a > b and c != d)

#3d program
if __name__ == '__main__':
    a = 2 * 2 + 2
    b = 2 * (2 + 2)
    print("3d program:")
    print(a)
    print(b)
    print(a == b)

#4th program
if __name__ == '__main__':
    a = '123.456'
    b = (float(a) * 10) % 10
    print("4th program:", int((float(a) * 10) % 10))