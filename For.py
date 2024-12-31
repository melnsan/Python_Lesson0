numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []         # список, состоящий из простых чисел
not_primes = []     # список, состоящий из составных чисел

for i in numbers:
    if i == 1:
        continue
    is_prime = True
    div_num = 0
    for j in range(2, i+1):
        if i % j == 0:
            div_num += 1
        if div_num == 2:
            is_prime = False
    if is_prime:
        primes.append(i)            # формирование списка, состоящего из простых чисел
    else:
        not_primes.append(i)        # формирование списка, состоящего из составных чисел
print(primes)
print(not_primes)