class Point2D:
    def __init__(self, x=0, y=0):
        self._x = x
        self._y = y

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        self._y = value

    def __repr__(self):
        return f"<Point x: {self.x}, Point y: {self.y}>"

    def __eq__(self, __o: object) -> bool:
        return self.x == __o.x and self.y == __o.y


if __name__ == "__main__":
    point = Point2D(8, 9)
    print(point)
