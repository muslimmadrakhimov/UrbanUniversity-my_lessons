def generate_password(n):
    password = ""
    # Перебор всех пар чисел от 1 до 20, исключая само число n
    for i in range(1, 21):
        if i == n:  # Пропускаем, если i равно n
            continue
        for j in range(i + 1, 21):
            if j == n:  # Пропускаем, если j равно n
                continue
            pair_sum = i + j
            # Проверяем, делится ли n на сумму пары
            if n % pair_sum == 0:
                password += str(i) + str(j)
    return password

# Пример: тестируем для чисел от 3 до 20
for n in range(3, 21):
    print(f"{n} - {generate_password(n)}")

