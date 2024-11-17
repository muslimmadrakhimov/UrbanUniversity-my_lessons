# Исходный список чисел
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

# Пустые списки для простых и непростых чисел
primes = []
not_primes = []

# Перебираем числа из списка numbers
for number in numbers:
    if number == 1:
        continue  # Пропускаем число 1, так как оно не является ни простым, ни составным

    # Изначально считаем число простым
    is_prime = True

    # Проверка делимости числа
    for i in range(2, number):
        if number % i == 0:  # Если число делится без остатка, оно не простое
            is_prime = False
            break  # Прерываем цикл, если найден делитель

    # В зависимости от того, простое ли число, добавляем его в соответствующий список
    if is_prime:
        primes.append(number)
    else:
        not_primes.append(number)

# Выводим списки простых и непростых чисел
print("Primes:", primes)
print("Not Primes:", not_primes)
