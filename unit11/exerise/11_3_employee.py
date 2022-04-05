import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    
    def setUp(self):
        self.my_employee = Employee('geek', 'boy', 5000)

    def test_give_default_raise(self):
        self.assertEqual(self.my_employee.money, 5000)

    def test_give_custom_raise(self):
        self.my_employee.give_raise()
        self.assertEqual(self.my_employee.money, 10000)

if __name__ == '__main__':
    unittest.main()
