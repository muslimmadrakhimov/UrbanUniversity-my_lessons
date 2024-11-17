class House:
    # Атрибут класса для хранения истории построенных объектов
    houses_history = []

    # Переопределяем метод __new__
    def __new__(cls, *args, **kwargs):
        # Добавляем название дома в историю
        cls.houses_history.append(args[0])  # Название дома в args[0]
        # Создаём новый объект
        return super().__new__(cls)

    # Инициализация объекта
    def __init__(self, name, floors):
        self.name = name  # Название дома
        self.floors = floors  # Количество этажей

    # Переопределяем метод __del__
    def __del__(self):
        # Сообщение при удалении объекта
        print(f"{self.name} снесён, но он останется в истории")


# Создание нескольких объектов класса House
h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)  # ['ЖК Эльбрус']

h2 = House('ЖК Акация', 20)
print(House.houses_history)  # ['ЖК Эльбрус', 'ЖК Акация']

h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)  # ['ЖК Эльбрус', 'ЖК Акация', 'ЖК Матрёшки']

# Удаление объектов
del h2
del h3

print(House.houses_history)  # ['ЖК Эльбрус', 'ЖК Акация', 'ЖК Матрёшки']

# В конце выполнения программы будет автоматически вызван __del__ для остальных объектов
