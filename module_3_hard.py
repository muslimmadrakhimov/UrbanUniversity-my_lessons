
def calculate_structure_sum(data_structure):
    total_sum = 0

    # Рекурсивная функция для обхода структуры данных
    def recursive_sum(item):
        nonlocal total_sum  # Для доступа к переменной total_sum внутри функции
        if isinstance(item, int):  # Если элемент - число
            total_sum += item
        elif isinstance(item, str):  # Если элемент - строка
            total_sum += len(item)
        elif isinstance(item, (list, tuple, set)):  # Если элемент - список, кортеж или множество
            for elem in item:
                recursive_sum(elem)  # Рекурсивно обрабатываем каждый элемент
        elif isinstance(item, dict):  # Если элемент - словарь
            for key, value in item.items():
                recursive_sum(key)  # Рекурсивно обрабатываем ключ
                recursive_sum(value)  # Рекурсивно обрабатываем значение

    # Запускаем рекурсивную обработку всей структуры данных
    recursive_sum(data_structure)

    return total_sum


# Тестируем на примере
data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)
