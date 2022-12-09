from api import SalaryEmployee
import unittest

class TestSalaryEmployee(unittest.TestCase): 
    def test_salary_employee_name(self):
        self.salary_employee = SalaryEmployee(2, 'John Smith', 85000)
        self.assertEqual(self.salary_employee.name, "John Smith")
    
    def test_salary_employee_identifier(self):
        self.salary_employee = SalaryEmployee(2, 'John Smith', 85000)
        self.assertEqual(self.salary_employee.identifier, 2)
    
    def test_salary_employee_pay_month(self):
        self.salary_employee = SalaryEmployee(2, 'John Smith', 85000)
        self.assertEqual(self.salary_employee.calculate_pay_month(), 85000/12)

# put your tests below
