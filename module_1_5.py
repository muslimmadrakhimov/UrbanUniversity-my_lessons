# Шаг 1: Создание переменной immutable_var с кортежем
immutable_var = (42, "hello", 3.14, True)

# Вывод кортежа на экран
print("Кортеж immutable_var:", immutable_var)

# Попытка изменения элемента кортежа
# immutable_var[0] = 100  # Приведет к ошибке TypeError, так как кортеж неизменяем

# Шаг 2: Создание изменяемого списка mutable_list
mutable_list = [42, "world", 2.71, False]

# Изменение элементов списка
mutable_list[0] = 100
mutable_list[1] = "Python"
mutable_list[3] = True

# Вывод изменённого списка на экран
print("Изменённый список mutable_list:", mutable_list)
