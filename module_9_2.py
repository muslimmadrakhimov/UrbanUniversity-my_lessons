# Даны два списка строк
first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

# Задача 1: Создать список, который содержит длины строк из списка first_strings,
# при условии, что длина строки не меньше 5 символов.

# Что мы делаем:
# 1. Мы будем перебирать каждую строку из списка `first_strings`.
# 2. Для каждой строки будем вычислять её длину при помощи функции len().
# 3. Если длина строки больше или равна 5 символам, то мы включим её длину в новый список.
# Для этого используем списочную сборку (list comprehension).

# Списочная сборка:
# Это способ создать новый список в одну строку, используя цикл for внутри квадратных скобок.
first_result = [len(word) for word in first_strings if len(word) >= 5]

# Подробное описание:
# [len(word) for word in first_strings if len(word) >= 5]
# - len(word) — это длина каждой строки, которую мы будем вычислять.
# - for word in first_strings — это цикл, который проходит по каждой строке в списке first_strings.
# - if len(word) >= 5 — условие: длина строки должна быть не меньше 5 символов.

# Таким образом, если строка в списке first_strings длиннее 5 символов, её длина попадет в first_result.

# Задача 2: Создать список пар (кортежей) слов, у которых одинаковая длина.
# Каждое слово из first_strings должно сравниваться с каждым словом из second_strings.

# Что мы делаем:
# 1. Будем сравнивать каждое слово из `first_strings` с каждым словом из `second_strings`.
# 2. Если длины слов совпадают, то будем добавлять их в виде пары (кортежа) в новый список.
# Для этого нам нужно использовать два цикла: внешний цикл и внутренний цикл.
# Внешний цикл проходит по списку `first_strings`, а внутренний по `second_strings`.

# Используем снова списочную сборку, но с двумя циклами.
second_result = [(word1, word2) for word1 in first_strings for word2 in second_strings if len(word1) == len(word2)]

# Подробное описание:
# [(word1, word2) for word1 in first_strings for word2 in second_strings if len(word1) == len(word2)]
# - (word1, word2) — это кортеж, который будет содержать два слова.
# - for word1 in first_strings — это внешний цикл, который проходит по каждому слову из first_strings.
# - for word2 in second_strings — это внутренний цикл, который проходит по каждому слову из second_strings.
# - if len(word1) == len(word2) — условие: длина слов должна быть одинаковой.
# Если длины слов одинаковы, пара (word1, word2) добавляется в список.

# Задача 3: Создать словарь, где ключом будет строка, а значением — её длина,
# при условии, что длина строки чётная.

# Что мы делаем:
# 1. Мы будем объединять два списка `first_strings` и `second_strings` в один.
# 2. Будем перебирать все строки из этого объединённого списка.
# 3. Для каждой строки будем вычислять её длину и проверять, является ли длина строки чётной.
# 4. Если длина строки чётная, добавляем строку и её длину в словарь, где строка будет ключом, а длина — значением.
# Для этого используем словарную сборку (dictionary comprehension).

# Объединение списков:
# Мы можем объединить два списка в один при помощи операции сложения (+).
# Например, first_strings + second_strings объединит два списка в один.

# Словарная сборка:
# Это способ создать словарь в одну строку, используя цикл for внутри фигурных скобок.

third_result = {word: len(word) for word in first_strings + second_strings if len(word) % 2 == 0}

# Подробное описание:
# {word: len(word) for word in first_strings + second_strings if len(word) % 2 == 0}
# - word: len(word) — это ключ-значение, где ключом является строка (word), а значением её длина (len(word)).
# - for word in first_strings + second_strings — это цикл, который проходит по объединённому списку first_strings и second_strings.
# - if len(word) % 2 == 0 — условие: длина строки должна быть чётной.
# Проверка на чётность: мы используем оператор % (остаток от деления на 2). Если остаток равен 0, значит длина строки чётная.

# Теперь выводим результаты работы программы на экран
print(first_result)  # Ожидаемый вывод: [10, 8, 8] — это длины строк, которые больше или равны 5 символам.
print(second_result)  # Ожидаемый вывод: [('Elon', 'Task'), ('Elon', 'Java'), ...] — пары слов одинаковой длины.
print(third_result)  # Ожидаемый вывод: {'Elon': 4, 'Musk': 4, ...} — словарь строк с чётными длинами.