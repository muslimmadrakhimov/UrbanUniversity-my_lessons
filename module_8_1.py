def add_everything_up(a, b):
    try:
        # Попытка сложить два значения
        # Если оба значения одного типа (например, оба числа или обе строки), операция пройдет успешно
        return a + b
    except TypeError:
        # Если типы данных различны (например, одно значение — число, другое — строка),
        # произойдет исключение TypeError, и мы попадем в блок except
        # В этом случае мы преобразуем оба значения в строки и объединяем их
        return str(a) + str(b)

# Примеры использования функции:

# Первый пример:
# Здесь '123.456' — это число (float), а 'строка' — это строка (str).
# Так как это разные типы, произойдет исключение, и функция вернет результат, объединив оба значения в строку.
print(add_everything_up(123.456, 'строка'))  # Вывод: 123.456строка

# Второй пример:
# 'яблоко' — это строка, а 4215 — это число (int).
# Снова разные типы данных, поэтому они будут объединены в строку: "яблоко4215".
print(add_everything_up('яблоко', 4215))  # Вывод: яблоко4215

# Третий пример:
# Оба аргумента — числа (float и int).
# В этом случае операция сложения выполнится корректно, и функция вернет результат их сложения.
print(add_everything_up(123.456, 7))  # Вывод: 130.456
