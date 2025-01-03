def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        row = []
        matrix.append(row)      # в пустой список добавляем пустые списки (строки) n раз
        for j in range(m):
            row.append(value)   # каждую строку (внутренний список) наполняем элементами m раз (столбцы)
    return matrix

def print_matrix (a):       # функция для печати строк матрицы (печатаем поштучно каждый элемент списка)
    for i in a:
        print(*i)       # * используется для распаковки, чтобы избавиться от [] при выводе
    print('')

result1 = get_matrix(2, 2, 5)
result2 = get_matrix(3, 5, 6)
result3 = get_matrix(4, 2, 7)
print_matrix(result1)
print_matrix(result2)
print_matrix(result3)