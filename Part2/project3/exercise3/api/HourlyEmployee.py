from api import Employee


class HourlyEmployee(Employee):
    """
    Employee who is payed for each working hour
    """

    def __init__(self, identifier: int, name: str, hour_rate: float):
        super().__init__(identifier, name)
        self.__hours_worked = 0
        self.__hour_rate = hour_rate

    @property
    def hours_worked(self) -> int:
        return self.__hours_worked

    @hours_worked.setter
    def hours_worked(self, hours_in_month: int) -> int:
        self.__hours_worked = hours_in_month
        return self.__hours_worked

    def calculate_pay_month(self) -> float:
        return self.hours_worked * self.__hour_rate
