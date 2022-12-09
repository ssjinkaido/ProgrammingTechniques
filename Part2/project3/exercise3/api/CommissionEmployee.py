from api import Employee, SalaryEmployee


class CommissionEmployee(SalaryEmployee):
    """Commission Employee payed using a fix annual salary, plus commissions"""

    def __init__(self, identifier: int, name: str, monthly_salary: float, commission: float):
        super().__init__(identifier, name, monthly_salary)
        self.__commission = commission

    def calculate_pay_month(self):
        fixed = super().calculate_pay_month()
        return fixed + self.__commission
