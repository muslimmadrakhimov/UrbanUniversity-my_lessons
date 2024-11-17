def get_multiplied_digits(number):
  """
  Функция рекурсивно перемножает все цифры целого числа.

  Args:
    number: Целое число.

  Returns:
    Произведение цифр числа.
  """

  str_number = str(number)  # Преобразуем число в строку
  if len(str_number) <= 1:  # Базовый случай: одна цифра
    return int(str_number)
  else:
    first = int(str_number[0])  # Первая цифра
    return first * get_multiplied_digits(int(str_number[1:]))  # Рекурсивный вызов

# Пример использования:
result = get_multiplied_digits(40203)
print(result)  # Вывод: 24