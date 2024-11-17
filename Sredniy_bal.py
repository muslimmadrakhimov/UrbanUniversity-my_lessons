grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

# Преобразуем множество в отсортированный список, чтобы имена соответствовали оценкам
students_sorted = sorted(students)

# Создадим пустой словарь для хранения средних баллов
student_avg_grades = {}

# Пройдемся по каждому ученику и посчитаем средний балл
for i, student in enumerate(students_sorted):
    avg_grade = sum(grades[i]) / len(grades[i])  # средний балл
    student_avg_grades[student] = avg_grade  # добавляем в словарь

# Выводим результат
print(student_avg_grades)
