from api import Employee
import unittest

# put your tests below
class TestEmployee(unittest.TestCase): 
    def test_employee_name(self):
        self.employee = Employee(1, "aaa")
        self.assertEqual(self.employee.name, "aaa")
        
    def test_employee_identifier(self):
        self.employee = Employee(1, "aaa")
        self.assertEqual(self.employee.identifier, 1)
