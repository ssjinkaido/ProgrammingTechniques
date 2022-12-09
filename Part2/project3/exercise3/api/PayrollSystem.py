from __future__ import annotations
from api import Employee
from typing import Dict

class PayrollSystem:
    """
    Human resource payroll system...
    """

    def __init__(self):
        self.__employees = {}

    @property
    def employees(self) -> Dict:
        return self.__employees

    def is_employee(self, employee: Employee) -> bool:
        """Check if a given employee is into the database"""

        return employee.identifier in self.__employees

    def add_employee(self, employee: Employee) -> None:
        """Add a new employee to the database"""

        if self.is_employee(employee):
            raise ValueError(f'employee {employee.identifier} already exists')

        self.__employees[employee.identifier] = employee

    def remove_employee(self, employee: Employee) -> None:
        """Remove a given employee from the database"""

        if not self.is_employee(employee):
            raise ValueError(f'employee {employee.identifier} is not in the database')

        del self.__employees[employee.identifier]

    def get_employee(self, identifier: int) -> Employee:
        return self.__employees[identifier]

    def calculate_pay_month(self) -> dict[int, float]:
        """Calculates and return the pay into a dictionary"""
        print("Here")
        result = {}

        for employee in self.__employees.values():
            result[employee.identifier] = employee.calculate_pay_month()

        return result

    def calculate_payroll(self) -> float:
        """Calculates and return the total payroll for all employees"""

        result = 0

        for employee in self.__employees.values():
            result = result + employee.calculate_pay_month()

        return result

    def generate_identifier(self) -> int:
        """Generate an unused employee identifier"""
        if len(self.__employees) == 0:
            return 1
        max_key = max(self.__employees)
        return 1 + max_key
