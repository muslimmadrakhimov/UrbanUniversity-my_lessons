# Подключаем библиотеку sqlite3 для работы с базой данных
import sqlite3

# ШАГ 1: Создаем (или подключаемся к) базу данных not_telegram.db
# Если файл базы данных отсутствует, он будет создан автоматически.
connection = sqlite3.connect('not_telegram.db')

# ШАГ 2: Создаем объект курсора. Курсор позволяет выполнять SQL-запросы.
cursor = connection.cursor()

# ШАГ 3: Создаем таблицу Users, если она еще не существует
# Таблица содержит пять колонок: id, username, email, age и balance.
creat_table_query = ("""
CREATE TABLE IF NOT EXISTS Users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,    -- Первичный ключ, уникальный идентификатор записи
    username TEXT NOT NULL,                  -- Имя пользователя, обязательное текстовое поле
    email TEXT NOT NULL,                     -- Email, обязательное текстовое поле
    age INTEGER,                             -- Возраст пользователя, целое число
    balance INTEGER NOT NULL                 -- Баланс пользователя, обязательное целое число
);
"""
cursor.execute(create_table_query)

# ШАГ 4: Заполняем таблицу 10 пользователями

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
insert_query = """
INSERT INTO Users (username, email, age, balance)
VALUES (?, ?, ?, ?);
"""
cursor.executemany(insert_query, users_data)

# ШАГ 5: Обновляем баланс у каждой 2-й записи, начиная с 1-й, на 500

update_query = """
UPDATE Users
SET balance = 500
WHERE id IN (1, 3, 5, 7, 9);
"""
cursor.execute(update_query)


# ШАГ 6: Удаляем каждую 3-ю запись, начиная с 1-й

delete_query = """
DELETE FROM Users
WHERE id IN (1, 4, 7, 10);
"""
cursor.execute(delete_query)

# ШАГ 7: Выбираем записи, где возраст не равен 60
# Используем SELECT для извлечения данных из таблицы с условием age != 60.
select_query = """
SELECT username, email, age, balance
FROM Users
WHERE age != 60;
"""
cursor.execute(select_query)

# Сохраняем результат выборки в переменную
records = cursor.fetchall()

# ШАГ 8:
# В цикле проходим по каждой строке результата и красиво форматируем вывод.
for record in records:
    print(f"Имя: {record[0]} | Почта: {record[1]} | Возраст: {record[2]} | Баланс: {record[3]}")

# ШАГ 9: Сохраняем изменения в базе данных
connection.commit()

# ШАГ 10: Закрываем соединение с базой данных

connection.close()

