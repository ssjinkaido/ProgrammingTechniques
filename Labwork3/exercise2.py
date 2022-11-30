from exercise1 import Point2D


class Robot:
    def __init__(self, name: str = "John", point: Point2D = Point2D()) -> None:
        self._name = name
        self._point = point

    def _get_name(self) -> str:
        return self._name

    def _set_name(self, value) -> None:
        self._name = value

    def _get_point(self) -> Point2D:
        return self._point

    def _set_point(self, value) -> None:
        self._point = value

    def __repr__(self):
        return f"<Robot name: {self._get_name()}, Point a: {self._point._get_x()}, Point y: {self._point._get_y()}>"


if __name__ == "__main__":
    point = Point2D(8, 9)
    robot = Robot(name="John", point=point)
    print(robot)
