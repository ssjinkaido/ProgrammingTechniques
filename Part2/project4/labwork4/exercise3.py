from abc import abstractmethod, ABC
class CoffeeShop:
    def __init__(self, name: str):
        self.__name = name

    @property
    def name(self):
        return self.__name

    

class DeliveryService(ABC):
    @abstractmethod
    def takeaway(self) -> str:
        pass

    
class A(CoffeeShop, DeliveryService):
    def takeaway(self) -> str:
        return "Delivery at most 30 minutes"

class B(CoffeeShop):
    pass


if __name__ == "__main__":
    # def display_dev(coffee_with_delivery: Union[CoffeeShop, DeliveryService])->None:
    #     print(f"{coffee_with_delivery.name}: {coffee_with_delivery.takeaway()}")
    
    # def display_without_dev(coffee_shop:CoffeeShop) -> None:
    #     print(f"{coffee_shop.name}, no delivery")

    # def display(cs: CoffeeShop|Union[CoffeeShop, DeliveryService])->None:
    #     if isinstance(cs, DeliveryService):
    #         display_dev(cs)
    #     else:
    #         display_without_dev(cs)
    a = A('A')
    b = B('B')
    print(f'CoffeeShop {a.name}: {a.takeaway()}')
    print(f'CoffeeShop {b.name}, not service')
#neu 1 class co 1 method, ma class con k dung duoc, thi phai vut method day di va chuyen xuong class con(bat cu class con nao xai duoc)
#con khong thi vi pham liskov
