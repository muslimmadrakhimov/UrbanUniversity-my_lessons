class Product:
    def __init__(self, name, weight, category):
        """
        Инициализатор для создания нового товара.

        Аргументы:
        name -- название продукта (строка)
        weight -- вес продукта (число с плавающей точкой)
        category -- категория продукта (строка)
        """
        self.name = name  # Название продукта
        self.weight = weight  # Вес продукта
        self.category = category  # Категория продукта

    def __str__(self):
        """
        Метод для получения строкового представления объекта.
        Возвращает строку в формате '<название>, <вес>, <категория>'.
        """
        return f'{self.name}, {self.weight}, {self.category}'


class Shop:
    def __init__(self):
        """
        Инициализатор магазина. Устанавливает имя файла для хранения товаров.
        """
        self.__file_name = 'products.txt'  # Имя файла, в который будут записываться товары

    def get_products(self):
        """
        Метод для чтения всех товаров из файла.
        Открывает файл products.txt, читает его содержимое и возвращает его в виде строки.
        Если файла не существует, возвращает пустую строку.
        """
        try:
            # Открываем файл для чтения
            with open(self.__file_name, 'r', encoding='utf-8') as file:
                return file.read().strip()  # Читаем содержимое и убираем лишние пробелы и переносы строк
        except FileNotFoundError:
            # Если файл не найден, возвращаем пустую строку
            return ''

    def add(self, *products):
        """
        Метод для добавления новых товаров в файл.
        Принимает любое количество объектов Product. Добавляет их в файл, если товара с таким именем еще нет.

        Аргументы:
        products -- одно или несколько объектов класса Product.
        """
        # Считываем текущие товары из файла
        current_products = self.get_products()

        # Создаем множество для хранения имен уже добавленных товаров
        current_product_names = set()
        if current_products:  # Если файл не пустой
            for line in current_products.split('\n'):  # Проходим по каждой строке файла
                product_data = line.split(', ')  # Разделяем строку на части по запятым
                if product_data:
                    current_product_names.add(product_data[0])  # Добавляем название товара в множество

        # Открываем файл для дозаписи (append)
        with open(self.__file_name, 'a', encoding='utf-8') as file:
            for product in products:  # Проходим по всем переданным продуктам
                if product.name not in current_product_names:
                    # Если товара с таким названием еще нет, добавляем его в файл
                    file.write(str(product) + '\n')
                    current_product_names.add(product.name)  # Обновляем множество добавленных товаров
                else:
                    # Если товар уже существует, выводим сообщение
                    print(f'Продукт {product} уже есть в магазине')


# Пример использования:
if __name__ == "__main__":
    # Создаем объект магазина
    s1 = Shop()

    # Создаем объекты продуктов
    p1 = Product('Potato', 50.5, 'Vegetables')
    p2 = Product('Spaghetti', 3.4, 'Groceries')
    p3 = Product('Potato', 5.5, 'Vegetables')

    # Выводим информацию о продукте p2
    print(p2)  # Результат: Spaghetti, 3.4, Groceries

    # Добавляем товары в магазин
    s1.add(p1, p2, p3)

    # Считываем и выводим все товары из файла
    print(s1.get_products())  # Выведет все товары, записанные в файл
