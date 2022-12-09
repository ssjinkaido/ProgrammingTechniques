from api import HourlyEmployee
import unittest
# put your tests below
class TestHourlyEmployee(unittest.TestCase): 
    def test_hourly_employee_name(self):
        self.hourly_employee = HourlyEmployee(2, 'Jane Doe', 15)
        self.assertEqual(self.hourly_employee.name, "Jane Doe")
    
    def test_hourly_employee_identifier(self):
        self.hourly_employee = HourlyEmployee(2, 'Jane Doe', 15)
        self.assertEqual(self.hourly_employee.identifier, 2)
    
    def test_hourly_employee_pay_month(self):
        self.hourly_employee = HourlyEmployee(2, 'Jane Doe', 15)
        self.hourly_employee.hours_worked = 42
        self.assertEqual(self.hourly_employee.calculate_pay_month(), 42*15)
