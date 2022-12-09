from abc import ABC, abstractmethod


class Employee:
    """Define an employee, from its identifier and name"""

    def __init__(self, identifier: int, name: str) -> None:
        self.__identifier = identifier
        self.__name = name

    @property
    def identifier(self) -> int:
        return self.__identifier

    @property
    def name(self) -> str:
        return self.__name

    @abstractmethod
    def calculate_pay_month(self) -> float:
        return 0.0
