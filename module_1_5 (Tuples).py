immutable_var = (1, 2, 'a', 'b', 'c', [5, 6]) # инициализируем переменную и присваиваем ей значения кортежа
print('Immutable tuple: ', immutable_var) # выводим весь кортеж
print('Immutable tuple: ', immutable_var[2]) # выводим 3-й элемент кортежа (а)
print('Immutable tuple: ', immutable_var[-1:]) # выводим последний элемент кортежа ([5, 6])
immutable_var[5][1] = 15 # меняем элемент кортежа - список [5, 6] на [5, 15]
print('Immutable tuple: ', immutable_var)

#immutable_var[0] = 15 # Будет ошибка, т.к. кортеж является неизменяемым типом
#print('Immutable tuple: ', immutable_var)

mutable_list = [11, 2, 'a', 'b']             # присваиваем значения списка
print('Mutable list: ', mutable_list)

mutable_list.append('Appended')
print(11 in mutable_list)
print('apple' in mutable_list)
mutable_list[2] = 'changed item'
print(mutable_list)
mutable_list.append(True)
print(mutable_list)
mutable_list.extend('test')   # если в скобках только одно значение, то вставляется каждый символ этого значения через запятую
print(mutable_list)
mutable_list.extend(['test', '+'])
print(mutable_list)
mutable_list.remove(True)
print(mutable_list)

a = mutable_list.pop(4)     # pop вырезает из списка значение по индексу и дает возможность записать в переменную
print('Mutable list: ', mutable_list)
print(a)

"""Задайте переменные разных типов данных:
  - Создайте переменную immutable_var и присвойте ей кортеж из нескольких элементов разных типов данных.
  - Выполните операции вывода кортежа immutable_var на экран.

3. Изменение значений переменных:
  - Попытайтесь изменить элементы кортежа immutable_var. Объясните, почему нельзя изменить значения элементов кортежа.

4. Создание изменяемых структур данных:
  - Создайте переменную mutable_list и присвойте ей список из нескольких элементов.
  - Измените элементы списка mutable_list.
  - Выведите на экран измененный список mutable_list.

"""