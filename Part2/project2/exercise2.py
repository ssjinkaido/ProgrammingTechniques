## up to you...
## define a class named Vegetable
class Vegetable:
    def __init__(self, name: str = "") -> None:
        self.__name = name

    @property
    def name(self) -> str:
        return self.__name


## then instantiate two objects,
tomato = Vegetable(name="tomato")
lettuce = Vegetable(name="lettuce")
## and then print their name

print(tomato.name)
print(lettuce.name)
