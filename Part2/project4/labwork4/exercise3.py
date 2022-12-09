from abc import abstractmethod
class CoffeeShop:
    def __init__(self, name: str):
        self.__name = name

    @property
    def name(self):
        return self.__name

    @abstractmethod
    def takeaway(self) -> str:
        pass
    
class A(CoffeeShop):
    def takeaway(self) -> str:
        return "Delivery at most 30 minutes"


class B(CoffeeShop):
    def takeaway(self) -> str:
        raise Exception('We do not have takeaway service')

def call_takeaway(coffee_shop: CoffeeShop):
    return coffee_shop.takeaway()


if __name__ == "__main__":
    a = A('A')
    b = B('B')
    print(call_takeaway(a))
    print(call_takeaway(b))
    print(f'CoffeeShop {a.name}: {a.takeaway()}')
    print(f'CoffeeShop {b.name}: {b.takeaway()}')
