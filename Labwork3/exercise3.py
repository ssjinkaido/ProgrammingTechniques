from exercise1 import Point2D
from exercise2 import Robot
from typing import List, Tuple


class Board:
    def __init__(
        self,
        rows: int,
        columns: int,
        point_exit: Point2D,
        robots_list: List[Robot],
        grid: List[List[int]],
    ) -> None:
        self._rows = rows
        self._columns = columns
        self._point_exit = point_exit
        self._robots_list = robots_list
        self._grid = grid

    def _get_rows(self) -> int:
        return self._rows

    def _set_rows(self, value) -> None:
        self._rows = value

    def _get_columns(self) -> int:
        return self._columns

    def _set_columns(self, value) -> None:
        self._columns = value

    def _get_point_exit(self) -> Point2D:
        return self._point_exit

    def _set_point_exit(self, value) -> None:
        self._point_exit = value

    def grid(self) -> List[List[int]]:
        return self._grid

    def _set_grid(self, value) -> None:
        self._grid = value

    def __repr__(self):
        return f"<Rows: {self._rows}, Columns: {self._columns}, Point exit: {self._point_exit}, Robots list: {self._robots_list}>"

    def add_robot(self, robot: Robot):
        self._robots_list.append(robot)

    def remove_robot(self, index: int):
        del self._robots_list[index]

    def is_inside(self, x: int, y: int) -> bool:
        return x >= 0 and x < self._rows and y >= 0 and y < self._columns

    def is_not_walled(self, x: int, y: int) -> bool:
        if not self.is_inside(x, y):
            return True
        return self._grid[x][y]

    def is_robot_position(self, x: int, y: int, robots: List[Robot]) -> bool:
        for robot in robots:
            if robot._get_point() == Point2D(x, y):
                return True
        return False

    def is_valid(self, x: int, y: int, robots: List[Robot]) -> bool:
        if robots:
            if (self.is_inside(x, y)) and (self.is_robot_position(x, y, robots)):
                return False

            elif (self.is_inside(x, y)) and (not self.is_robot_position(x, y, robots)):
                if self.is_not_walled(x, y):
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

    def check_points_visited(self, point: Point2D, visited: set) -> bool:
        for p in visited:
            if point._get_x() == p[0] and point._get_y() == p[1]:
                return True
        return False

    def reachable(self, robot: Robot, robots: List[Robot]) -> List:
        path_found = False
        queue = []
        results = []
        visited = set()
        parent = dict()
        parent[tuple([robot._get_point()._get_x(), robot._get_point()._get_y()])] = None
        visited.add(tuple([robot._get_point()._get_x(), robot._get_point()._get_y()]))
        queue.append(tuple([robot._get_point()._get_x(), robot._get_point()._get_y()]))
        while queue:
            current_point = queue.pop(0)
            if (
                current_point[0] == self._point_exit._get_x()
                and current_point[1] == self._point_exit._get_y()
            ):
                path_found = True
                break
            adjacent_points = self.neighbors_list(current_point, robots)
            # print("Neighbors", adjacent_points)

            for next_point in adjacent_points:
                if not self.check_points_visited(next_point, visited):
                    queue.append(tuple([next_point._get_x(), next_point._get_y()]))
                    parent[
                        tuple([next_point._get_x(), next_point._get_y()])
                    ] = current_point
                    visited.add(tuple([next_point._get_x(), next_point._get_y()]))
            # print("queue: ", queue)
            # print("visited", visited)
            #

        point_exit = [self._point_exit._get_x(), self._point_exit._get_y()]
        if path_found == True:
            results.append(tuple([point_exit[0], point_exit[1]]))
            while parent[tuple([point_exit[0], point_exit[1]])] is not None:
                results.append(parent[tuple([point_exit[0], point_exit[1]])])
                point_exit = parent[tuple([point_exit[0], point_exit[1]])]
            results.reverse()
        return results

    def move_robot(self) -> None:
        all_paths = []
        num_robots = len(self._robots_list)
        for i in range(num_robots - 1):
            path_robot = self.reachable(
                self._robots_list[i], self._robots_list[i : num_robots - 2]
            )
            all_paths.append(path_robot)
        all_paths.append(self.reachable(self._robots_list[-1], []))

        for i in range(len(all_paths)):
            print(f"Path for robot {i+1}: {all_paths[i]}")


if __name__ == "__main__":
    point1 = Point2D(5, 6)
    point2 = Point2D(6, 1)
    point3 = Point2D(10, 2)
    point4 = Point2D(2, 8)
    robot1 = Robot(name="Alice", point=point1)
    robot2 = Robot(name="Bob", point=point2)
    robot3 = Robot(name="Lisa", point=point3)
    robot4 = Robot(name="Florida", point=point4)
    grid = [
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
    board = Board(
        rows=11,
        columns=11,
        point_exit=Point2D(10, 1),
        robots_list=[robot1, robot2, robot3, robot4],
        grid=grid,
    )
    board.move_robot()
