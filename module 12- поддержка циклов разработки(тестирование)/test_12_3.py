from runner_and_tournament import Runner, Tournament
from runner import Runner as Run
import unittest


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        walks = Run('Victor')
        for _ in range(10):
            walks.walk()
        self.assertEqual(walks.distance, 50)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        run = Run('Sergio')
        for _ in range(10):
            run.run()
        self.assertEqual(run.distance, 100)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        runner_1 = Run('Anna')
        runner_2 = Run('Blanka')
        for _ in range(10):
            runner_1.run()
            runner_2.walk()
        self.assertNotEqual(runner_1.distance, runner_2.distance)


class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner_1 = Runner('Усейн', 10)
        self.runner_2 = Runner('Андрей', 9)
        self.runner_3 = Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        for result in cls.all_results.values():
            print({key: str(value) for key, value in result.items()})

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_race_1(self):
        tour = Tournament(90, self.runner_1, self.runner_3)
        self.all_results.update({'race_1': tour.start()})
        result = max(self.all_results)
        result_indent = self.all_results[result]
        indent = max(result_indent)
        self.assertTrue(result_indent[indent] == 'Ник')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_race_2(self):
        tour = Tournament(90, self.runner_2, self.runner_3)
        self.all_results.update({'race_2': tour.start()})
        result = max(self.all_results)
        result_indent = self.all_results[result]
        indent = max(result_indent)
        self.assertTrue(result_indent[indent] == 'Ник')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_race_3(self):
        tour = Tournament(90, self.runner_1, self.runner_2, self.runner_3)
        self.all_results.update({'race_3': tour.start()})
        result = max(self.all_results)
        result_indent = self.all_results[result]
        indent = max(result_indent)
        self.assertTrue(result_indent[indent] == 'Ник')