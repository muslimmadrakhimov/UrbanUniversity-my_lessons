
#  Цель: освоить методы, которые содержит класс TestCase.

import unittest
from runners import Runner, Tournament

class TournamentTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Этот метод вызывается один раз перед всеми тестами.
        # Инициализируем атрибут класса для хранения результатов.
        cls.all_results = {}

    def setUp(self):
        # Этот метод выполняется перед каждым тестом.
        # Создаем несколько бегунов с разными скоростями
        self.runner_usain = Runner("Усэйн", 10)  # Усэйн с большой скоростью
        self.runner_andrey = Runner("Андрей", 9)  # Андрей с меньшей скоростью
        self.runner_nick = Runner("Ник", 3)  # Ник с самой низкой скоростью

    @classmethod
    def tearDownClass(cls):
        # Этот метод выполняется после всех тестов.
        # Печатаем результаты каждого теста.
        for result in cls.all_results.values():
            # Для каждого результата выводим его в читаемом формате:
            # словарь вида {место: имя бегуна}
            readable_result = {place: str(runner) for place, runner in result.items()}
            print(readable_result)  # Печатаем результат

    def test_usain_nick(self):
        # Тест забега между Усэйном и Ником
        tournament = Tournament(90, self.runner_usain, self.runner_nick)  # Создаем турнир с дистанцией 90
        result = tournament.start()  # Запускаем турнир
        self.__class__.all_results["test_usain_nick"] = result  # Сохраняем результат в атрибут класса
        self.assertTrue(result[max(result.keys())] == "Ник")  # Проверяем, что Ник финиширует последним

    def test_andrey_nick(self):
        # Тест забега между Андреем и Ником
        tournament = Tournament(90, self.runner_andrey, self.runner_nick)
        result = tournament.start()
        self.__class__.all_results["test_andrey_nick"] = result
        self.assertTrue(result[max(result.keys())] == "Ник")  # Ник всегда последний

    def test_usain_andrey_nick(self):
        # Тест забега между Усэйном, Андреем и Ником
        tournament = Tournament(90, self.runner_usain, self.runner_andrey, self.runner_nick)
        result = tournament.start()
        self.__class__.all_results["test_usain_andrey_nick"] = result
        self.assertTrue(result[max(result.keys())] == "Ник")  # Ник всегда последний

if __name__ == "__main__":
    unittest.main()  # Запуск всех тестов



