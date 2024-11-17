def get_matrix(n, m, value):
    # Если n или m меньше или равно 0, возвращаем пустую матрицу
    if n <= 0 or m <= 0:
        return []

    # Создаем пустой список для матрицы
    matrix = []

    # Внешний цикл для строк (n раз)
    for i in range(n):
        # Создаем строку, состоящую из m столбцов, заполненных значением value
        row = []
        for j in range(m):
            row.append(value)
        # Добавляем строку в матрицу
        matrix.append(row)

    # Возвращаем полученную матрицу
    return matrix


# Примеры вызова функции
result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)

# Вывод результатов
print(result1)
print(result2)
print(result3)
