class Point2D:
    def __init__(self, x: int = 0, y: int = 0):
        self._x = x
        self._y = y

    def _get_x(self) -> int:
        return self._x

    def _set_x(self, value) -> None:
        self._x = value

    def _get_y(self) -> int:
        return self._y

    def set_y(self, value) -> None:
        self._y = value

    def __repr__(self) -> None:
        return f"<Point x: {self._get_x()}, Point y: {self._get_y()}>"

    def __eq__(self, __o: object) -> bool:
        return self._x == __o._x and self._y == __o._y


if __name__ == "__main__":
    point = Point2D(8, 9)
    print(point)
