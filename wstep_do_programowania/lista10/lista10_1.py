import re
import unittest

'''zad1'''
email = 'python2020@gusun_tomail.com'
try:
    match = re.search('usun_to', email)
except SyntaxError:
    print('Nie znaleziono frazy do usuniecia')
else:
    new_mail = re.sub(match.group(), '', email)
print(new_mail)


'''zad2'''


class Employee:
    def __init__(self, first_name, last_name, annual_salary):
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = annual_salary
        self.default_raise = 2000

    def give_raise(self, employee_raise=2000):
        return self.annual_salary + employee_raise


class EmployeeTests(unittest.TestCase):

    def setUp(self):
        self.employee = Employee('Adam', 'Bednarski', 0)

    def test_give_default_raise(self):
        self.assertEqual(self.employee.annual_salary + 2000,
                         self.employee.give_raise(), 'error')

    def test_give_custom_raise(self):
        self.assertEqual(self.employee.annual_salary + 7000,
                         self.employee.give_raise(7000), 'error')


if __name__ == '__main__':
    unittest.main()
