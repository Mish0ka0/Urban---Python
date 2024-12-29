from runner_and_tournament import Runner, Tournament
import unittest


class TournamentTest(unittest.TestCase):

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

    def test_race_1(self):
        tour = Tournament(90, self.runner_1, self.runner_3)
        self.all_results.update({'race_1': tour.start()})
        result = max(self.all_results)
        result_indent = self.all_results[result]
        indent = max(result_indent)
        self.assertTrue(result_indent[indent] == 'Ник')

    def test_race_2(self):
        tour = Tournament(90, self.runner_2, self.runner_3)
        self.all_results.update({'race_2': tour.start()})
        result = max(self.all_results)
        result_indent = self.all_results[result]
        indent = max(result_indent)
        self.assertTrue(result_indent[indent] == 'Ник')

    def test_race_3(self):
        tour = Tournament(90, self.runner_1, self.runner_2, self.runner_3)
        self.all_results.update({'race_3': tour.start()})
        result = max(self.all_results)
        result_indent = self.all_results[result]
        indent = max(result_indent)
        self.assertTrue(result_indent[indent] == 'Ник')


if __name__ == '__main__':
    unittest.main()
