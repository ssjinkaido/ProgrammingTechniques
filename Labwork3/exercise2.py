from exercise1 import Point2D
class Robot():
    def __init__(self, name, point:Point2D):
        self.name = name
        self.point = point
    
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def point(self):
        return self._point

    @point.setter
    def point(self, value):
        self._point = value

    def __repr__(self):
        return f"<Robot name: {self.name}, Point a: {self.point.x}, Point y: {self.point.y}>"

if __name__ == "__main__":
    point = Point2D(8, 9)
    robot = Robot(name='Alice', point=point)
    print(robot)