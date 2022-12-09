from api import PayrollSystem
# put your tests below
import unittest
from unittest.mock import MagicMock, patch
class TestPayrollSystem(unittest.TestCase):
    # @patch('api.SalaryEmployee')
    # def test_add_salary_employee(self, mock_salary_employee):
    #     payroll_system = PayrollSystem()
    #     instance = mock_salary_employee.return_value
    #     instance.identifier = 1
    #     instance.name = 'aaa'
    #     instance.annual_salary = 85000
    #     payroll_system.add_employee(instance)
    #     self.assertEqual(payroll_system.employees[1], instance)

    def create_instance(self, identifier, name, salary):
        instance = MagicMock()
        instance.identifier = identifier
        instance.name = name
        instance.calculate_pay_month.return_value = salary
        return instance

    def test_add_employee_using_magic_mock(self):
        payroll_system = PayrollSystem()
        payroll_system.add_employee(self.create_instance(1, 'aaa', 100))
        self.assertEqual(len(payroll_system.employees), 1)

    def test_remove_employee_using_magic_mock(self):
        payroll_system = PayrollSystem()
        payroll_system.add_employee(self.create_instance(1, 'aaa', 100))
        self.assertEqual(len(payroll_system.employees), 1)
        payroll_system.remove_employee(payroll_system.employees[1])
        self.assertEqual(len(payroll_system.employees), 0)
        
    def test_get_employee_using_magic_mock(self):
        payroll_system = PayrollSystem()
        instance = self.create_instance(1, 'aaa', 100)
        payroll_system.add_employee(instance)
        self.assertEqual(payroll_system.get_employee(1), instance)

    def test_is_employee_using_magic_mock(self):
        payroll_system = PayrollSystem()
        instance = self.create_instance(1, 'aaa', 100)
        payroll_system.add_employee(instance)
        self.assertEqual(payroll_system.is_employee(instance), 1)

    def test_calculate_pay_month_using_magic_mock(self):
        payroll_system = PayrollSystem()
        payroll_system.add_employee(self.create_instance(1, 'aaa', 100))
        payroll_system.add_employee(self.create_instance(2, 'bbb', 1000))
        result = payroll_system.calculate_pay_month()
        self.assertEqual(result[1], 100)
        self.assertEqual(result[2], 1000)

    def test_calculate_payroll_using_magic_mock(self):
        payroll_system = PayrollSystem()
        payroll_system.add_employee(self.create_instance(1, 'aaa', 100))
        payroll_system.add_employee(self.create_instance(2, 'bbb', 1000))
        payroll_system.add_employee(self.create_instance(3, 'ccc', 2500))
        result = payroll_system.calculate_payroll()
        self.assertEqual(result, 3600)

    def test_generate_identifier_using_magic_mock(self):
        payroll_system = PayrollSystem()
        self.assertEqual(payroll_system.generate_identifier(), 1, "1")

    def test_generate_identifier_with_multiple_employees_using_magic_mock(self):
        payroll_system = PayrollSystem()
        payroll_system.add_employee(self.create_instance(1, 'aaa', 100))
        payroll_system.add_employee(self.create_instance(2, 'bbb', 1000))
        self.assertEqual(payroll_system.generate_identifier(), 3, "3")
