from api import Employee


class SalaryEmployee(Employee):
    """
    Salary employee has a fix salary, payed each month with the same amount.
    """

    def __init__(self, identifier: int, name: str, annual_salary: float):
        """"
        Initializes a Salary Employee

        Notice that the annual salary is given for one year...
        """

        super().__init__(identifier, name)
        self.__annual_salary = annual_salary

    def calculate_pay_month(self) -> float:
        return self.__annual_salary / 12.0
