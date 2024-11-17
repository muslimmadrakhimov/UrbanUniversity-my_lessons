class House:
    def __init__(self, name, number_of_floors):
        self.name = name  # Название здания
        self.number_of_floors = number_of_floors  # Количество этажей

    # Магический метод для возвращения длины (количество этажей)
    def __len__(self):
        return self.number_of_floors

    # Магический метод для строкового представления объекта
    def __str__(self):
        return f"Название: {self.name}, кол-во этажей: {self.number_of_floors}"

# Пример использования
h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

# Вывод строкового представления объектов (работает __str__)
print(h1)
print(h2)

# Получение количества этажей (работает __len__)
print(len(h1))
print(len(h2))
