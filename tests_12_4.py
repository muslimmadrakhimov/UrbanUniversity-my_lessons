

# Цель: получить опыт использования простейшего логирования совместно с тестами.

# Задача "Логирование бегунов":


import unittest
import logging
from runners1 import Runner  # Подключите класс Runner из вашего основного кода

# Настраиваем логирование
logging.basicConfig(
    filename="runner_tests.log",  # Имя файла для логов
    level=logging.INFO,  # Уровень логирования - INFO
    filemode="w",  # Режим записи - с заменой (w)
    encoding="utf-8",  # Кодировка
    format="%(asctime)s | %(levelname)s | %(message)s"  # Формат вывода
)

# Класс тестов для Runner
class RunnerTest(unittest.TestCase):
    def test_walk(self):
        """Тест на проверку ошибки при отрицательной скорости"""
        try:
            # Здесь speed передается отрицательным, чтобы вызвать ValueError
            r1 = Runner("Вася", -5)
            r1.walk()
            logging.info('"test_walk" выполнен успешно')
        except ValueError as e:
            logging.warning("Неверная скорость для Runner")
            logging.warning(e)

    def test_run(self):
        """Тест на проверку ошибки при неправильном типе имени"""
        try:
            # Здесь name передается как число, чтобы вызвать TypeError
            r2 = Runner(123, 5)
            r2.run()
            logging.info('"test_run" выполнен успешно')
        except TypeError as e:
            logging.warning("Неверный тип данных для объекта Runner")
            logging.warning(e)

# Запускаем тесты
if __name__ == "__main__":
    unittest.main()
