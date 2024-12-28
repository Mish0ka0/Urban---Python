import unittest
from runner import Runner


class RunnerTest(unittest.TestCase):

    def test_walk(self):
        walks = Runner('Victor')
        for _ in range(10):
            walks.walk()
        self.assertEqual(walks.distance, 50)

    def test_run(self):
        run = Runner('Sergio')
        for _ in range(10):
            run.run()
        self.assertEqual(run.distance, 100)

    def test_challenge(self):
        runner_1 = Runner('Anna')
        runner_2 = Runner('Blanka')
        for _ in range(10):
            runner_1.run()
            runner_2.walk()
        self.assertNotEqual(runner_1.distance, runner_2.distance)


if __name__ == '__main__':
    unittest.main()