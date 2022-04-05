import unittest
from city_functions import city_name


class CityTest(unittest.TestCase):
    def test_city_name(self):
        ret_name = city_name('shanghai', 'china')
        self.assertEqual(ret_name , 'Shanghai , China')
        
    def test_city_name_populatio(self):
        ret_name = city_name('shanghai', 'china', '50000')
        print(ret_name)
        self.assertEqual(ret_name, 'Shanghai, China - Population 50000')

if __name__ == '__main__':
    unittest.main()
