# Цель: научится использовать функции внутри запросов языка SQL и использовать их в решении задачи.

# Задача "Средний баланс пользователя":


import sqlite3  # Подключаем библиотеку для работы с SQLite

# Подключаемся к базе данных (создаем файл not_telegram.db, если его нет)
connection = sqlite3.connect('not_telegram.db')
cursor = connection.cursor()  # Создаем объект курсора для выполнения SQL-запросов

# 1. Удаляем старую таблицу Users (если она существует) и создаем заново
# Это сбросит все данные и автонумерацию id
cursor.execute("DROP TABLE IF EXISTS Users;")  # Удаляем таблицу
create_table_query = """
CREATE TABLE Users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,  -- Уникальный идентификатор, автоматически увеличивается
    username TEXT NOT NULL,                -- Имя пользователя, обязательно для заполнения
    email TEXT NOT NULL,                   -- Email пользователя, обязательно для заполнения
    age INTEGER,                           -- Возраст пользователя
    balance INTEGER NOT NULL               -- Баланс пользователя, обязательно для заполнения
);
"""
cursor.execute(create_table_query)  # Создаем таблицу

# 2. Добавление данных в таблицу

users_data = [
    ("User1", "example1@gmail.com", 10, 1000),
    ("User2", "example2@gmail.com", 20, 1000),
    ("User3", "example3@gmail.com", 30, 1000),
    ("User4", "example4@gmail.com", 40, 1000),
    ("User5", "example5@gmail.com", 50, 1000),
    ("User6", "example6@gmail.com", 60, 1000),
    ("User7", "example7@gmail.com", 70, 1000),
    ("User8", "example8@gmail.com", 80, 1000),
    ("User9", "example9@gmail.com", 90, 1000),
    ("User10", "example10@gmail.com", 100, 1000),
]

# SQL-запрос для вставки данных
insert_query = """
INSERT INTO Users (username, email, age, balance)
VALUES (?, ?, ?, ?);
"""
cursor.executemany(insert_query, users_data)  # Добавляем сразу несколько записей

# 3. Обновление балансов у каждой 2-й записи начиная с 1ой
# Каждая 2-я запись (где id делится на 2 без остатка) получает баланс 500
update_query = """
UPDATE Users
SET balance = 500
WHERE id % 2 = 1;
"""
cursor.execute(update_query)

# 4. Удаление каждой 3-й записи начиная с 1ой
# Удаляем записи, где id делится на 3 без остатка
delete_query = """
DELETE FROM Users
WHERE id % 3 = 1;
"""
cursor.execute(delete_query)

# 5. Удаление записи с id=6
# Если запись с id=6 осталась, удаляем ее
delete_id_query = """
DELETE FROM Users
WHERE id = 6;
"""
cursor.execute(delete_id_query)

# 6. Подсчёт общего количества пользователей
# Считаем количество строк в таблице (пользователей)
count_query = """
SELECT COUNT(*) FROM Users;
"""
cursor.execute(count_query)
total_users = cursor.fetchone()[0]  # Получаем количество пользователей

# 7. Подсчёт суммы всех балансов
# Считаем сумму всех балансов
sum_query = """
SELECT SUM(balance) FROM Users;
"""
cursor.execute(sum_query)
all_balances = cursor.fetchone()[0]  # Получаем сумму балансов

# 8. Вычисление среднего баланса
# Если есть пользователи, вычисляем средний баланс, иначе выводим 0
if total_users > 0:
    average_balance = all_balances / total_users
else:
    average_balance = 0

# 9. Вывод результатов
print("Средний баланс:", average_balance)

# 10. Завершаем изменения и закрываем соединение
connection.commit()  # Подтверждаем все изменения в базе данных
connection.close()   # Закрываем соединение с базой данных


