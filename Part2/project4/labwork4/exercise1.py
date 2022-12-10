from __future__ import annotations
class Address:
    def __init__(self, city: str, zip_code:int):
        self.__city = city
        self.__zip_code = zip_code

    @property
    def city(self) -> str:
        return self.__city

    @city.setter
    def city(self, value:str) -> None:
        self.__city = value
    
    @property
    def zip_code(self) -> int:
        return self.__zip_code

    @zip_code.setter
    def zip_code(self, value:int) -> None:
        self.__zip_code = value

    def change_address(self, city:str, zip_code: int) -> None:
        self.__city = city
        self.__zip_code = zip_code
        
class CoffeeShop:
    def __init__(self, name: str, address: Address):
        self.__name = name
        self.__address = address

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, value: str) -> None:
        self.__name = value
    
    @property
    def address(self) -> Address:
        return self.__address

    @address.setter(self, address: Address)-> None:
        self.__address = address
    
if __name__ == '__main__':
    cs = CoffeeShop('La Viet', Address('Ha Noi', 111000))
    print(f'CoffeeShop name is "{cs.name}"')
    print(f'CoffeeShop is in "{cs.address.city}"')
    print(f'CoffeeShop zip code is {cs.address.zip_code}')
    cs.address = Address('Neuville de Poitou', 86170)
    cs.address.change_address('Neuville de Poitou', 86170)
    print(f'CoffeeShop name is "{cs.name}"')
    print(f'CoffeeShop is in "{cs.address.city}"')
    print(f'CoffeeShop zip code is {cs.address.zip_code}')
