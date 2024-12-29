import logging
import unittest
from rt_with_exceptions import Runner


class RunnerTest(unittest.TestCase):

    def test_walk(self):
        try:
            walks = Runner('Victor', -5)
            for _ in range(10):
                walks.walk()
            self.assertEqual(walks.distance, 50)
            logging.info('"test_walk" выполнен успешно')
        except ValueError:
            logging.warning('Неверная скорость для  Runner', exc_info=True)

    def test_run(self):
        try:
            run = Runner(2)
            for _ in range(10):
                run.run()
            self.assertEqual(run.distance, 100)
            logging.info('"test_run" выполнен успешно')
        except TypeError:
            logging.warning('Неверный тип данных для объекта Runner', exc_info=True)

    def test_challenge(self):
        runner_1 = Runner('Anna')
        runner_2 = Runner('Blanka')
        for _ in range(10):
            runner_1.run()
            runner_2.walk()
        self.assertNotEqual(runner_1.distance, runner_2.distance)


logging.basicConfig(level=logging.INFO, filemode='w', encoding='utf-8', filename='runner_tests.log',
                    format='%(asctime)s | %(levelname)s | %(message)s')


if __name__ == "__main__":
    unittest.main()
