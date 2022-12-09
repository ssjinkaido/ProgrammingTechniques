from __future__ import annotations
from enum import Enum


class Vehicle:
    """Represents a vehicle with or without engine"""

    def __init__(self: Vehicle, max_person_capacity: int = 0, max_speed: float = 0):
        """Constructor of Vehicle class"""
        self.__max_person_capacity = max_person_capacity
        self.__max_speed = max_speed

    @property
    def max_person_capacity(self: Vehicle) -> int:
        """Getter of the maximum person capacity of a Vehicle instance"""
        return self.__max_person_capacity

    @property
    def max_speed(self: Vehicle) -> float:
        """Getter of the maximum speed of a Vehicle instance"""
        return self.__max_speed


class Engine:
    """Represents an engine"""

    Fuel = Enum(
        "Fuel", ["diesel", "gasoline", "kerosene", "coal", "electricity", "solar"]
    )
    """Enumeration of different Fuels"""

    def __init__(self: Engine, fuel: Engine.Fuel, consumption: float) -> None:
        """Constructor of an Engine"""
        self.__fuel = fuel
        self.__consumption = consumption

    @property
    def fuel(self: Engine) -> Engine.Fuel:
        """Getter of the Fuel of this Engine instance"""
        return self.__fuel

    @property
    def average_consumption(self: Engine) -> float:
        """Returns the average consumption of this Engine instance"""
        return self.__consumption

    @staticmethod
    def having_engine(obj: object):
        """Predicate that returns if an object instance is an engine or not"""
        return isinstance(obj, Engine)


class Bicycle(Vehicle):
    """Represents a Bicycle, a vehicle for one person with no engine"""

    def __init__(self: Bicycle, max_speed: float = 99):
        Vehicle.__init__(self, 1, max_speed)


class Donkey(Vehicle):
    """Represents a Donkey, a vehicle for one person with no engine"""

    def __init__(self: Donkey, max_speed: float = 21):
        Vehicle.__init__(self, 1, max_speed)


class Car(Vehicle, Engine):
    """Represents a Car, a vehicle made to transport some people with an engine"""

    def __init__(
        self: Car,
        max_person_capacity: int = 5,
        max_speed: float = 250,
        fuel: Engine.Fuel = Engine.Fuel.diesel,
        consumption: float = 6,
    ):
        Vehicle.__init__(self, max_person_capacity, max_speed)
        Engine.__init__(self, fuel, consumption)


class Boat(Vehicle, Engine):
    """
    Represents a Boat, a vehicle made to transport some people with an engine
    """

    def __init__(
        self: Boat,
        max_person_capacity: int = 5,
        max_speed: float = 40,
        fuel: Engine.Fuel = Engine.Fuel.diesel,
        consumption: float = 50,
    ):
        Vehicle.__init__(self, max_person_capacity, max_speed)
        Engine.__init__(self, fuel, consumption)


class Airplane(Vehicle, Engine):
    """
    Represents an Airplane, a vehicle made to transport many people
    with an engine
    """

    def __init__(
        self: Airplane,
        max_person_capacity: int = 300,
        max_speed: float = 1000,
        consumption: float = 100,
    ):
        Vehicle.__init__(self, max_person_capacity, max_speed)
        Engine.__init__(self, Engine.Fuel.kerosene, consumption)


if __name__ == "__main__":

    def miles_to_km(miles):
        """Transforms a distance in miles to a distance in kilometers"""
        return 1.852 * miles

    vehicles = [
        Bicycle(),
        Car(4, 180),
        Car(),
        Boat(12, miles_to_km(12)),
        Boat(4, miles_to_km(25)),
        Airplane(),
        Airplane(2, 3000),
    ]

    for vehicle in vehicles:

        def printEngine(obj):
            if Engine.having_engine(obj):
                return (
                    f"with an Engine using {obj.fuel.name} with "
                    + f"average consumption about {obj.average_consumption}"
                )
            return "without an Engine"

        print(f"A {vehicle.__class__.__name__}:")
        print(f"- {printEngine(vehicle)}")
        print(
            f"- that can transport up to " + f"{vehicle.max_person_capacity} person(s)"
        )
        print(f"- with maximum speed {vehicle.max_speed}")
