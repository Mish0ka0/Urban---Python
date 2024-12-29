import unittest
# from module_12_1 import RunnerTest
# from module_12_2 import TournamentTest
from test_12_3 import RunnerTest, TournamentTest


test_mod = unittest.TestSuite()
test_mod.addTest(unittest.TestLoader().loadTestsFromTestCase(RunnerTest))
test_mod.addTest(unittest.TestLoader().loadTestsFromTestCase(TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(test_mod)
