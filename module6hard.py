import math

# Родительский класс Figure
class Figure:
    sides_count = 0  # Число сторон у фигуры

    def __init__(self, color, *sides):
        # Инкапсулированные атрибуты
        self.__color = list(color)
        if len(sides) != self.sides_count:
            self.__sides = [1] * self.sides_count  # Если неверное количество сторон
        else:
            self.__sides = list(sides)
        # Публичный атрибут
        self.filled = False

    # Метод для получения цвета
    def get_color(self):
        return self.__color

    # Служебный метод проверки валидности цвета
    def __is_valid_color(self, r, g, b):
        return all(isinstance(i, int) and 0 <= i <= 255 for i in (r, g, b))

    # Метод для установки цвета
    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    # Служебный метод проверки сторон
    def __is_valid_sides(self, *new_sides):
        return (
            len(new_sides) == self.sides_count and
            all(isinstance(side, int) and side > 0 for side in new_sides)
        )

    # Метод для получения сторон
    def get_sides(self):
        return self.__sides

    # Метод для установки новых сторон
    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)

    # Метод для получения периметра
    def __len__(self):
        return sum(self.__sides)

# Класс Circle (Круг)
class Circle(Figure):
    sides_count = 1  # У круга 1 "сторона" - длина окружности

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        # Радиус можно вычислить из длины окружности: L = 2 * pi * r
        self.__radius = self.get_sides()[0] / (2 * math.pi)

    # Метод для получения площади круга
    def get_square(self):
        return math.pi * self.__radius ** 2

# Класс Triangle (Треугольник)
class Triangle(Figure):
    sides_count = 3  # У треугольника три стороны

    # Метод для получения площади треугольника (по формуле Герона)
    def get_square(self):
        a, b, c = self.get_sides()
        s = sum(self.get_sides()) / 2  # Полупериметр
        return math.sqrt(s * (s - a) * (s - b) * (s - c))

# Класс Cube (Куб)
class Cube(Figure):
    sides_count = 12  # У куба 12 рёбер

    def __init__(self, color, *sides):
        # Переопределяем список сторон, делая их одинаковыми
        if len(sides) == 1:
            sides = sides * 12  # Одно значение распространяем на все рёбра
        super().__init__(color, *sides)

    # Метод для получения объёма куба
    def get_volume(self):
        # Кубический объём: V = a^3, где a - длина ребра
        return self.get_sides()[0] ** 3

# Пример использования

circle1 = Circle((200, 200, 100), 10)  # Цвет и длина окружности
cube1 = Cube((222, 35, 130), 6)  # Цвет и длина рёбер

# Проверка изменения цветов
circle1.set_color(55, 66, 77)  # Изменится
print(circle1.get_color())  # [55, 66, 77]

cube1.set_color(300, 70, 15)  # Не изменится
print(cube1.get_color())  # [222, 35, 130]

# Проверка изменения сторон
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
print(cube1.get_sides())  # [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6]

circle1.set_sides(15)  # Изменится
print(circle1.get_sides())  # [15]

# Проверка периметра (длины окружности)
print(len(circle1))  # 15

# Проверка объёма куба
print(cube1.get_volume())  # 216

