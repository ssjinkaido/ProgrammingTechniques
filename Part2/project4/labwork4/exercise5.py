from abc import ABC, abstractmethod
class ICoffeeShop(ABC):
    def __init__(self, name: str):
        self.__name = name

    @property
    def name(self):
        return self.__name

    @abstractmethod
    def get_payment(self):
        pass

    @abstractmethod
    def deliver_coffee(self):
        pass

    
class CoffeeShop(ICoffeeShop):
    def get_payment(self):
        print(f"{self._ICoffeeShop__name} gets the payment")

    def deliver_coffee(self):
        print(f"{self._ICoffeeShop__name} delivers the coffee")

class ICustomer(ABC):
    def __init__(self, name: str):
        self.__name = name
        
    @property
    def name(self):
        return self.__name
        
    @abstractmethod
    def make_payment(self):
        pass

    @abstractmethod
    def receive_coffee(self):
        pass


class Customer(ICustomer):

    def make_payment(self):
        print(f"{self._ICustomer__name} makes the payment")

    def receive_coffee(self):
        print(f"{self._ICustomer__name} receives the coffee")

class IDelivery(ABC):
    def __init__(self, customer: ICustomer, coffee_shop: ICoffeeShop):
        self.__customer = customer
        self.__coffee_shop = coffee_shop

    @abstractmethod
    def delivers(self):
        pass


class Delivery(IDelivery):

    def delivers(self):
        self._IDelivery__customer.make_payment()
        self._IDelivery__coffee_shop.get_payment()
        self._IDelivery__coffee_shop.deliver_coffee()
        self._IDelivery__customer.receive_coffee()


if __name__ == '__main__':
    Delivery(Customer('Uncle Bob'), CoffeeShop('La Viet')).delivers()
