# Подключаем библиотеку sqlite3 для работы с базой данных
import sqlite3

# ШАГ 1: Создаем (или подключаемся к) базу данных not_telegram.db
# Если файл базы данных отсутствует, он будет создан автоматически.
connection = sqlite3.connect('not_telegram.db')

# ШАГ 2: Создаем объект курсора. Курсор позволяет выполнять SQL-запросы.
cursor = connection.cursor()

# ШАГ 3: Создаем таблицу Users, если она еще не существует
# Таблица содержит пять колонок: id, username, email, age и balance.
cursor.execute('''
CREATE TABLE IF NOT EXISTS Users (
    id INTEGER PRIMARY KEY,    -- Первичный ключ, уникальный идентификатор записи
    username TEXT NOT NULL,    -- Имя пользователя, обязательное текстовое поле
    email TEXT NOT NULL,       -- Email, обязательное текстовое поле
    age INTEGER,               -- Возраст пользователя, целое число
    balance INTEGER NOT NULL   -- Баланс пользователя, обязательное целое число
)
''')
print("Таблица Users успешно создана (если её не было ранее).")

# ШАГ 4: Заполняем таблицу 10 пользователями
# Если таблица уже была заполнена ранее, этот шаг можно пропустить, чтобы не дублировать данные.
users = [
    ("User1", "example1@gmail.com", 10, 1000),
    ("User2", "example2@gmail.com", 20, 1000),
    ("User3", "example3@gmail.com", 30, 1000),
    ("User4", "example4@gmail.com", 40, 1000),
    ("User5", "example5@gmail.com", 50, 1000),
    ("User6", "example6@gmail.com", 60, 1000),
    ("User7", "example7@gmail.com", 70, 1000),
    ("User8", "example8@gmail.com", 80, 1000),
    ("User9", "example9@gmail.com", 90, 1000),
    ("User10", "example10@gmail.com", 100, 1000)
]

# Вставляем данные пользователей в таблицу
cursor.executemany('''
INSERT INTO Users (username, email, age, balance)
VALUES (?, ?, ?, ?)
''', users)
print("Таблица заполнена пользователями.")

# ШАГ 5: Обновляем баланс у каждой 2-й записи, начиная с 1-й, на 500
# Здесь используется условие id % 2 = 1, которое выбирает записи с нечетным id.
cursor.execute('''
UPDATE Users
SET balance = 500
WHERE id % 2 = 1
''')
print("Баланс обновлен у каждого 2-го пользователя (начиная с 1-го).")

# ШАГ 6: Удаляем каждую 3-ю запись, начиная с 1-й
# Условие id % 3 = 0 выбирает записи, где id делится на 3 без остатка.
cursor.execute('''
DELETE FROM Users
WHERE id % 3 = 0
''')
print("Каждая 3-я запись удалена из таблицы.")

# ШАГ 7: Выбираем записи, где возраст не равен 60
# Используем SELECT для извлечения данных из таблицы с условием age != 60.
cursor.execute('''
SELECT username, email, age, balance
FROM Users
WHERE age != 60
''')

# Сохраняем результат выборки в переменную
result = cursor.fetchall()

# ШАГ 8: Выводим записи на экран
# В цикле проходим по каждой строке результата и красиво форматируем вывод.
print("Результат выборки пользователей с возрастом не равным 60:")
for row in result:
    print(f"Имя: {row[0]} | Почта: {row[1]} | Возраст: {row[2]} | Баланс: {row[3]}")

# ШАГ 9: Сохраняем изменения в базе данных
connection.commit()

# ШАГ 10: Закрываем соединение с базой данных
# Это важно для освобождения ресурсов и предотвращения повреждения базы данных.
connection.close()
print("Соединение с базой данных закрыто.")
