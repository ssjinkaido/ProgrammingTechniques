from __future__ import annotations
from abc import ABC, abstractmethod
class ICoffeeShop(ABC):
    @property
    @abstractmethod
    def name(self: ICoffeeShop) -> str:
        ...

    @abstractmethod
    def get_payment(self: ICoffeeShop)->None:
        ...

    @abstractmethod
    def deliver_coffee(self: ICoffeeShop)->None:
        ...

    
class CoffeeShop(ICoffeeShop):
    def __init__(self: CoffeeShop, name: str):
        self.__name = name

    @property
    def name(self) -> str:
        return self.__name

    def get_payment(self: CoffeeShop):
        print(f"{self.__name} gets the payment")

    def deliver_coffee(self: CoffeeShop):
        print(f"{self.__name} delivers the coffee")

class ICustomer(ABC):  
    @property
    @abstractmethod
    def name(self: ICustomer) -> str:
        ...


    @abstractmethod
    def make_payment(self: ICustomer)->None:
        ...

    @abstractmethod
    def receive_coffee(self: ICustomer)->None:
        ...


class Customer(ICustomer):
    def __init__(self, name: str):
        self.__name = name
        
    @property
    def name(self) -> str:
        return self.__name

    def make_payment(self):
        print(f"{self.__name} makes the payment")

    def receive_coffee(self):
        print(f"{self.__name} receives the coffee")

class IDelivery(ABC):
    @abstractmethod
    def delivers(self: IDelivery, coffee_shop: ICoffeeShop, customer: ICustomer)->None:
        ...


class Delivery(IDelivery):

    def delivers(self: Delivery, coffee_shop: ICoffeeShop, customer: ICustomer):
        customer.make_payment()
        coffee_shop.get_payment()
        coffee_shop.deliver_coffee()
        customer.receive_coffee()


if __name__ == '__main__':
    Delivery().delivers(CoffeeShop('La Viet'), Customer('Uncle Bob'))
