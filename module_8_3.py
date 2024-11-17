# Определяем класс исключения для некорректного VIN номера
# Мы наследуем его от встроенного класса Exception, чтобы создать свое собственное исключение
class IncorrectVinNumber(Exception):
    # Конструктор класса, который принимает сообщение об ошибке
    def __init__(self, message):
        # Атрибут message будет хранить текст ошибки
        self.message = message
        # Вызываем конструктор базового класса Exception с этим сообщением
        super().__init__(self.message)

# Определяем класс исключения для некорректных номеров автомобиля
# Этот класс также наследуется от Exception
class IncorrectCarNumbers(Exception):
    # Конструктор класса, который принимает сообщение об ошибке
    def __init__(self, message):
        # Атрибут message будет хранить текст ошибки
        self.message = message
        # Вызываем конструктор базового класса Exception с этим сообщением
        super().__init__(self.message)

# Теперь создадим основной класс для представления автомобиля
class Car:
    # Конструктор класса (метод __init__), который вызывается при создании объекта
    # Он принимает три параметра: model (модель автомобиля), vin (VIN номер), и numbers (автомобильные номера)
    def __init__(self, model, vin, numbers):
        # Атрибут model указывает на модель автомобиля, это публичный атрибут
        self.model = model
        # Проверяем корректность VIN номера с помощью приватного метода __is_valid_vin
        # Если VIN корректен, он сохраняется в приватный атрибут __vin
        if self.__is_valid_vin(vin):
            self.__vin = vin
        # Проверяем корректность номера автомобиля с помощью приватного метода __is_valid_numbers
        # Если номера корректны, они сохраняются в приватный атрибут __numbers
        if self.__is_valid_numbers(numbers):
            self.__numbers = numbers

    # Приватный метод для проверки VIN номера
    # Этот метод проверяет, является ли переданный vin_number корректным
    def __is_valid_vin(self, vin_number):
        # Проверяем, является ли vin_number целым числом
        if not isinstance(vin_number, int):
            # Если тип данных неправильный, выбрасываем исключение IncorrectVinNumber
            raise IncorrectVinNumber('Некорректный тип vin номер')
        # Проверяем, находится ли vin_number в диапазоне от 1000000 до 9999999
        if not (1000000 <= vin_number <= 9999999):
            # Если vin_number не соответствует диапазону, выбрасываем исключение IncorrectVinNumber
            raise IncorrectVinNumber('Неверный диапазон для vin номера')
        # Если все проверки пройдены, возвращаем True, что означает корректность VIN номера
        return True

    # Приватный метод для проверки номера автомобиля
    # Этот метод проверяет, является ли переданный numbers корректным
    def __is_valid_numbers(self, numbers):
        # Проверяем, является ли numbers строкой (тип данных str)
        if not isinstance(numbers, str):
            # Если это не строка, выбрасываем исключение IncorrectCarNumbers
            raise IncorrectCarNumbers('Некорректный тип данных для номеров')
        # Проверяем, состоит ли строка numbers ровно из 6 символов
        if len(numbers) != 6:
            # Если длина строки не равна 6, выбрасываем исключение IncorrectCarNumbers
            raise IncorrectCarNumbers('Неверная длина номера')
        # Если все проверки пройдены, возвращаем True, что означает корректность номера
        return True

# Пример использования класса Car и перехват исключений
# Мы создадим несколько объектов Car и проверим различные ситуации

# Попытка создать первый автомобиль с правильными данными
try:
    # Передаем корректную модель, VIN номер и номера автомобиля
    first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
    # Если возникает исключение IncorrectVinNumber, выводим сообщение ошибки
    print(exc.message)
except IncorrectCarNumbers as exc:
    # Если возникает исключение IncorrectCarNumbers, выводим сообщение ошибки
    print(exc.message)
else:
    # Если исключений нет, значит объект создан успешно, выводим сообщение
    print(f'{first.model} успешно создан')

# Попытка создать второй автомобиль с некорректным VIN номером
try:
    # Передаем модель, некорректный VIN номер (слишком маленький), но корректные номера автомобиля
    second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
    # Если возникает исключение IncorrectVinNumber, выводим сообщение ошибки
    print(exc.message)
except IncorrectCarNumbers as exc:
    # Если возникает исключение IncorrectCarNumbers, выводим сообщение ошибки
    print(exc.message)
else:
    # Если исключений нет, значит объект создан успешно, выводим сообщение
    print(f'{second.model} успешно создан')

# Попытка создать третий автомобиль с некорректными номерами
try:
    # Передаем модель, корректный VIN номер, но некорректные номера (неправильная длина)
    third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
    # Если возникает исключение IncorrectVinNumber, выводим сообщение ошибки
    print(exc.message)
except IncorrectCarNumbers as exc:
    # Если возникает исключение IncorrectCarNumbers, выводим сообщение ошибки
    print(exc.message)
else:
    # Если исключений нет, значит объект создан успешно, выводим сообщение
    print(f'{third.model} успешно создан')
