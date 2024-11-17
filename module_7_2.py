# Определяем функцию custom_write, которая принимает два аргумента:
# 1. file_name — имя файла, в который нужно записать строки.
# 2. strings — список строк, которые мы будем записывать в файл.
def custom_write(file_name, strings):
    # Создаем пустой словарь, который будет хранить информацию о позициях строк.
    strings_positions = {}

    # Открываем файл для записи. 'w' — режим записи. encoding='utf-8' — используем кодировку UTF-8,
    # чтобы поддерживать все символы (например, русские буквы, специальные символы).
    file = open(file_name, 'w', encoding='utf-8')

    try:
        # Проходим по списку строк 'strings'. Используем enumerate, чтобы получить
        # сразу и индекс (номер строки), и саму строку. Нумерация начинается с 1.
        for i, string in enumerate(strings, start=1):
            # Метод tell() возвращает текущую позицию в файле в байтах.
            # Эта позиция указывает, где начнется запись следующей строки.
            position = file.tell()

            # Записываем строку в файл. Добавляем символ новой строки '\n',
            # чтобы каждая строка начиналась с новой строки в файле.
            file.write(string + '\n')

            # Добавляем в словарь позицию строки. Ключем словаря будет кортеж:
            # (номер строки, начальная позиция в байтах).
            # Значением будет сама строка.
            strings_positions[(i, position)] = string
    finally:
        # Закрываем файл после завершения записи, освобождаем ресурсы.
        file.close()

    # Возвращаем заполненный словарь, где хранятся позиции строк.
    return strings_positions


# Тестируем нашу функцию custom_write.

# Создаем список строк, который будем записывать в файл.
info = [
    'Text for tell.',  # Первая строка.
    'Используйте кодировку utf-8.',  # Вторая строка.
    'Because there are 2 languages!',  # Третья строка.
    'Спасибо!'  # Четвертая строка.
]

# Вызываем нашу функцию, передаем имя файла и список строк для записи.
# Функция возвращает словарь с информацией о том, где каждая строка была записана.
result = custom_write('test.txt', info)

# Выводим полученный словарь на экран.
# Каждый элемент словаря представляет собой кортеж с номером строки и начальной позицией,
# а также строку, которая была записана.
for elem in result.items():
    print(elem)
