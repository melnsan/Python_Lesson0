# Работа со словарями:
my_dict = {'Alex' : 1986, 'Andy' : 1989} # присваиваем переменной значения словаря
print('Initial dictionary: ', my_dict)
print('Existing value: ', my_dict['Alex'])                     # выводим запись с ключем Alex
print(my_dict.get('Sonya', 'Киски по имени Соня еще не было'))
my_dict['Alex'] = 1990
my_dict['Sonya'] = 1996                     # обращаемся по несуществующему ключу, поэтому он добавляется в словарь
my_dict.update({'Sveta': 1998,
               'Vika': 2000})
print('Updated dictionary: ', my_dict)
a = my_dict.pop('Sveta')            # вырезаем из словаря и присваиваем переменной а
print('Deleted value: ', a)
print('Dictionary without Sveta: ', my_dict)                  # выводим весь словарь
print('Existed keys: ', my_dict.keys())             # выводим список ключей

# Работа с множествами:
my_set = {1, 3, 5, 11, 5, 'Alex', True, (1, 2, 3)}
print('Initial set: ', my_set)
my_set.add(False)
my_set.add(8)
my_set.discard((1, 2, 3))
print('Set with added two values and deleted (1, 2, 3) tuple: ',  my_set)