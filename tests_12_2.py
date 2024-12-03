import runner_and_tournament as rt
import unittest


class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}


    def setUp(self):
        self.runner1 = rt.Runner('Усэйн', 10)
        self.runner2 = rt.Runner('Андрей', 9)
        self.runner3 = rt.Runner('Ник', 3)


    @classmethod
    def tearDownClass(cls):
        for key, value in cls.all_results.items():
            print(f'{key}: {value}')


    def test1_Tournament(self):
        race = rt.Tournament(90, self.runner1, self.runner3)
        result = race.start()
        self.assertTrue(result[max(result.keys())].name == 'Ник')
        self.all_results['Первый забег'] = {place: runner.name for place, runner in result.items()}


    def test2_Tournament(self):
        race = rt.Tournament(90, self.runner2, self.runner3)
        result = race.start()
        self.assertTrue(result[max(result.keys())].name == 'Ник')
        self.all_results['Второй забег'] = {place: runner.name for place, runner in result.items()}


    def test3_Tournament(self):
        race = rt.Tournament(90, self.runner1, self.runner2, self.runner3)
        result = race.start()
        self.assertTrue(result[max(result.keys())].name == 'Ник')
        self.all_results['Третий забег'] = {place: runner.name for place, runner in result.items()}


if __name__ == "__main__":
    unittest.main()

