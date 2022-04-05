import unittest
from city_functions import city_name

class CityTest(unittest.TestCase):
    def test_city_name(self):
        ret_name = city_name('shanghai', 'china')
        self.assertEqual(ret_name, 'Shanghai , China')


if __name__ == '__main__':
    unittest.main()
