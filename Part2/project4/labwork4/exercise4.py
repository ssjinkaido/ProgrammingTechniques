from abc import ABC, abstractmethod


class ICoffeeShop(ABC):
    # traditional shops
    @abstractmethod
    def brew_machine_pour_over(self):
        pass

    # third wave shops
    @abstractmethod
    def brew_filter_coffee(self):
        pass

class ITraditional(ICoffeeShop):
    # traditional shops
    @abstractmethod
    def brew_by_espresso_machine(self):
        pass

class IThirdWave(ICoffeeShop):
    # third wave shops
    @abstractmethod
    def brew_by_hand_held_espresso_maker(self):
        print("brewing by hand held expresso maker")

class Traditional(ITraditional):
    def brew_by_espresso_machine(self):
        print("brewing by expresso machine")

    def brew_machine_pour_over(self):
        print("brewing maching pour over")

    def brew_filter_coffee(self):
        print("brewing filter coffee")

class ThirdWave(IThirdWave):
    def brew_by_hand_held_espresso_maker(self):
        print("brewing by hand held expresso maker")

    def brew_manual_pour_over(self):
        print("brewing manual pour over")

    def brew_filter_coffee(self):
        print("brewing filter coffee")


if __name__ == "__main__":
    def print_all(coffee_shop: ICoffeeShop):
        """Try all the methods..."""
        def handle_exception(func):
            """Print the exception if one is raised"""
            try:
                func()
            except NotImplementedError as exception:
                print(f'-> {exception}')

        handle_exception(coffee_shop.brew_by_espresso_machine)
        handle_exception(coffee_shop.brew_machine_pour_over)
        handle_exception(coffee_shop.brew_by_hand_held_espresso_maker)
        handle_exception(coffee_shop.brew_manual_pour_over)
        coffee_shop.brew_filter_coffee()

    print('For a Traditional Coffee Shop...')
    print_all(Traditional())
    print('')
    print('For a ThirdWave Coffee Shop...')
    print_all(ThirdWave())
