from api import CommissionEmployee
import unittest

# put your tests below
class TestCommissionEmployee(unittest.TestCase):
    def test_commission_employee_name(self):
        self.commission_employee = CommissionEmployee(2, "Kevin Bacon", 50000, 2500)
        self.assertEqual(self.commission_employee.name, "Kevin Bacon")

    def test_commission_employee_identifier(self):
        self.commission_employee = CommissionEmployee(2, "Kevin Bacon", 50000, 2500)
        self.assertEqual(self.commission_employee.identifier, 2)

    def test_commission_employee_pay_month(self):
        self.commission_employee = CommissionEmployee(2, "Kevin Bacon", 50000, 2500)
        self.assertEqual(
            self.commission_employee.calculate_pay_month(), 50000 / 12 + 2500
        )
