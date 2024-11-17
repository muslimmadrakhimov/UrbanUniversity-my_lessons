def print_params(a=1, b='строка', c=True):
    print(a, b, c)

# 1. Вызовы функции с разным количеством аргументов
print_params()  # 1, 'строка', True
print_params(b=25)  # 1, 25, True
print_params(c=[1, 2, 3])  # 1, 'строка', [1, 2, 3]

# 2. Распаковка параметров из списка и словаря
values_list = [42, 'Тест', False]
values_dict = {'a': 99, 'b': 'Python', 'c': [10, 20, 30]}

print_params(*values_list)  # 42, 'Тест', False
print_params(**values_dict)  # 99, 'Python', [10, 20, 30]

# 3. Распаковка + отдельные параметры
values_list_2 = [54.32, 'Строка']
print_params(*values_list_2, 42)  # 54.32, 'Строка', 42
