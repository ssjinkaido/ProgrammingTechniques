from exercise1 import Point2D
from exercise2 import Robot
from typing import List
import numpy as np
from typing import List, Tuple


class Board:
    def __init__(
        self, rows: int, columns: int, point_exit: Point2D, robots_list: List[Robot]
    ):
        self.rows = rows
        self.columns = columns
        self.point_exit = point_exit
        self.robots_list = robots_list
        self.grid = np.array(
            [
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            ]
        )

    @property
    def rows(self):
        return self._rows

    @rows.setter
    def rows(self, value):
        self._rows = value

    @property
    def columns(self):
        return self._columns

    @columns.setter
    def columns(self, value):
        self._columns = value

    @property
    def point_exit(self):
        return self._point_exit

    @point_exit.setter
    def point_exit(self, value):
        self._point_exit = value

    @property
    def grid(self):
        return self._grid

    @grid.setter
    def grid(self, value):
        self._grid = value

    def __repr__(self):
        return f"<Rows: {self.rows}, Columns: {self.columns}, Point exit: {self.point_exit}, Robots list: {self.robots_list}>"

    def add_robot(self, robot: Robot):
        self.robots_list.append(robot)

    def remove_robot(self, index: int):
        del self.robots_list[index]

    def is_inside(self, x: int, y: int) -> bool:
        return x >= 0 and x < self.rows and y >= 0 and y < self.columns

    def is_not_walled(self, x: int, y: int) -> bool:
        if not self.is_inside(x, y):
            return True
        return self.grid[x][y]

    def is_robot_position(self, x: int, y: int, robots: List[Robot]) -> bool:
        for robot in robots:
            if robot.point == Point2D(x, y):
                return True
        return False

    def is_valid(self, x: int, y: int, robots: List[Robot]) -> bool:
        if robots:
            if (self.is_inside(x, y)) and (self.is_robot_position(x, y, robots)):
                return False
            
            elif (self.is_inside(x, y)) and (not self.is_robot_position(x, y, robots)):
                if (self.is_not_walled(x, y)):
                    return True
                else:
                    return False               
            
        else:
            return self.is_inside(x, y) and self.is_not_walled(x, y)

    def neighbors_list(self, point: Tuple, robots: List[Robot]) -> List[Point2D]:
        neighbor_loc = []
        point_x = point[0]
        point_y = point[1]
        if self.is_valid(point_x, point_y - 1, robots):
            neighbor_loc.append(Point2D(point_x, point_y - 1))
        if self.is_valid(point_x, point_y + 1, robots):
            neighbor_loc.append(Point2D(point_x, point_y + 1))
        if self.is_valid(point_x - 1, point_y, robots):
            neighbor_loc.append(Point2D(point_x - 1, point_y))
        if self.is_valid(point_x + 1, point_y, robots):
            neighbor_loc.append(Point2D(point_x + 1, point_y))
        return neighbor_loc

    def check_points_visited(self, point: Tuple, visited: set) -> bool:
        for p in visited:
            if point.x == p[0] and point.y == p[1]:
                return True
        return False

    def reachable(self, robot: Robot, robots: List[Robot]) -> List:
        path_found = False
        queue = []
        results = []
        visited = set()
        parent = dict()
        parent[tuple([robot.point.x, robot.point.y])] = None
        visited.add(tuple([robot.point.x, robot.point.y]))
        queue.append(tuple([robot.point.x, robot.point.y]))
        n = 0
        while queue:
            current_point = queue.pop(0)
            if (
                current_point[0] == self.point_exit.x
                and current_point[1] == self.point_exit.y
            ):
                path_found = True
                break
            adjacent_points = self.neighbors_list(current_point, robots)
            # print("Neighbors", adjacent_points)

            for next_point in adjacent_points:
                if not self.check_points_visited(next_point, visited):
                    queue.append(tuple([next_point.x, next_point.y]))
                    parent[tuple([next_point.x, next_point.y])] = current_point
                    visited.add(tuple([next_point.x, next_point.y]))
            # print("queue: ", queue)
            # print("visited", visited)
            #

        point_exit = [self.point_exit.x, self.point_exit.y]
        if path_found == True:
            results.append(tuple([point_exit[0], point_exit[1]]))
            while parent[tuple([point_exit[0], point_exit[1]])] is not None:
                results.append(parent[tuple([point_exit[0], point_exit[1]])])
                point_exit = parent[tuple([point_exit[0], point_exit[1]])]
            results.reverse()
        return results

    def move_robot(self):
        all_paths = []
        num_robots = len(self.robots_list)
        for i in range(num_robots - 1):
            path_robot = self.reachable(
                self.robots_list[i], self.robots_list[i : num_robots - 2]
            )
            all_paths.append(path_robot)
        all_paths.append(self.reachable(self.robots_list[-1], []))

        for i in range(len(all_paths)):
            print(f"Path for robot {i}: {all_paths[i]}")


if __name__ == "__main__":
    point = Point2D(5, 6)
    point1 = Point2D(6, 1)
    point2 = Point2D(10, 2)
    point3 = Point2D(2, 8)
    robot = Robot(name="Alice", point=point)
    robot1 = Robot(name="Bob", point=point1)
    robot2 = Robot(name="Lisa", point=point2)
    robot3 = Robot(name="Florida", point=point3)
    board = Board(
        rows=11,
        columns=11,
        point_exit=Point2D(10, 1),
        robots_list=[robot, robot1, robot2, robot3],
    )
    # print(board.grid)
    # print(board)
    # board.add_robot(robot)
    # print(board)
    # board.remove_robot(1)
    # print(board)
    board.move_robot()
