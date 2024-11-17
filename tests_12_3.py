
# Цель: понять на практике как объединять тесты при помощи TestSuite. Научиться пропускать тесты при помощи встроенных в unittest декораторов.

import unittest
from runners import Runner, Tournament

# Декоратор для контроля пропуска тестов
def frozen_control(test_func):
    def wrapper(self, *args, **kwargs):
        if self.is_frozen:
            self.skipTest('Тесты в этом кейсе заморожены')
        else:
            return test_func(self, *args, **kwargs)
    return wrapper

class RunnerTest(unittest.TestCase):
    is_frozen = False  # Не заморожено

    def setUp(self):
        self.runner = Runner("Test Runner", 5)

    @frozen_control
    def test_run(self):
        self.runner.run()
        self.assertEqual(self.runner.distance, 10)

    @frozen_control
    def test_walk(self):
        self.runner.walk()
        self.assertEqual(self.runner.distance, 5)

    @frozen_control
    def test_challenge(self):
        self.runner.run()
        self.runner.walk()
        self.assertEqual(self.runner.distance, 15)

class TournamentTest(unittest.TestCase):
    is_frozen = True  # Заморожено

    def setUp(self):
        self.runner_usain = Runner("Усэйн", 10)
        self.runner_andrey = Runner("Андрей", 9)
        self.runner_nick = Runner("Ник", 3)

    @frozen_control
    def test_first_tournament(self):
        tournament = Tournament(90, self.runner_usain, self.runner_nick)
        result = tournament.start()
        self.assertTrue(result[max(result.keys())] == "Ник")

    @frozen_control
    def test_second_tournament(self):
        tournament = Tournament(90, self.runner_andrey, self.runner_nick)
        result = tournament.start()
        self.assertTrue(result[max(result.keys())] == "Ник")

    @frozen_control
    def test_third_tournament(self):
        tournament = Tournament(90, self.runner_usain, self.runner_andrey, self.runner_nick)
        result = tournament.start()
        self.assertTrue(result[max(result.keys())] == "Ник")

