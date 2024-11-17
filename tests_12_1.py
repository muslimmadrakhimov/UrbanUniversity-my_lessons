

# Цель: приобрести навык создания простейших Юнит-тестов


# test_runner.py

import unittest  # Подключаем модуль unittest для создания тестов.
from runner import Runner  # Импортируем класс Runner, который будем тестировать.


# Создаем класс RunnerTest, который будет содержать тесты.
class RunnerTest(unittest.TestCase):

    def test_walk(self):
        """Тестирование метода walk.

        Этот тест проверяет, что после 10 вызовов walk
        дистанция увеличивается до 50.
        """
        runner = Runner("Test Runner")  # Создаем объект класса Runner с именем "Test Runner".

        # Вызываем метод walk 10 раз.
        for _ in range(10):
            runner.walk()

        # Проверяем, что дистанция (distance) равна 50.
        # Метод assertEqual проверяет, что первое значение (runner.distance)
        # равно второму (50).
        self.assertEqual(runner.distance, 50, "Дистанция после ходьбы должна быть 50")

    def test_run(self):
        """Тестирование метода run.

        Этот тест проверяет, что после 10 вызовов run
        дистанция увеличивается до 100.
        """
        runner = Runner("Test Runner")  # Создаем объект класса Runner с именем "Test Runner".

        # Вызываем метод run 10 раз.
        for _ in range(10):
            runner.run()

        # Проверяем, что дистанция (distance) равна 100.
        # Если это условие не выполняется, тест не пройдет.
        self.assertEqual(runner.distance, 100, "Дистанция после бега должна быть 100")

    def test_challenge(self):
        """Тестирование различия в дистанции между бегом и ходьбой.

        Этот тест проверяет, что два объекта, использующие разные методы (run и walk),
        пройдут разное расстояние после 10 вызовов каждого метода.
        """
        runner1 = Runner("Runner 1")  # Создаем первый объект бегуна.
        runner2 = Runner("Runner 2")  # Создаем второй объект бегуна.

        # Вызываем метод run 10 раз у runner1 и walk 10 раз у runner2.
        for _ in range(10):
            runner1.run()  # Runner 1 использует метод run.
            runner2.walk()  # Runner 2 использует метод walk.

        # Проверяем, что дистанции у двух объектов разные.
        # Метод assertNotEqual проверяет, что значения не равны.
        self.assertNotEqual(runner1.distance, runner2.distance,
                            "Дистанция должна быть разной для бега и ходьбы")


# Проверяем, выполняется ли скрипт напрямую.
# Если да, то запускаем unittest.main(), который запускает все тесты в файле.
if __name__ == "__main__":
    unittest.main()
