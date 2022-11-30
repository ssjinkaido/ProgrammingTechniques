import numpy as np
from typing import List, Tuple


def neighbors_case_1(tray: np.ndarray, square: List) -> List[Tuple]:
    s = tuple(np.array(tray.shape) - 1)
    n = np.array([-1, 0, +1])
    rows = square[0] + n
    cols = square[1] + n
    neighbor_loc = [
        (x, y) for x in rows for y in cols if (0 <= x <= s[0]) & (0 <= y <= s[1])
    ]
    items_to_remove = [
        (square[0], square[1]),
        (square[0] - 1, square[1] - 1),
        (square[0] - 1, square[1] - 1),
        (square[0] + 1, square[1] - 1),
        (square[0] + 1, square[1] + 1),
    ]
    neighbor_loc = [i for i in neighbor_loc if i not in items_to_remove]
    neighbor_loc = [i for i in neighbor_loc if tray[i[0]][i[1]] == False]
    return neighbor_loc


def neighbors_case_2(tray: np.ndarray, squares_list: List) -> List[List[Tuple]]:
    s = tuple(np.array(tray.shape) - 1)
    n = np.array([-1, 0, +1])
    squares_list_neighbor = []
    for square in squares_list:
        rows = square[0] + n
        cols = square[1] + n
        neighbor_loc = [
            [x, y] for x in rows for y in cols if (0 <= x <= s[0]) & (0 <= y <= s[1])
        ]
        items_to_remove = [
            [square[0], square[1]],
            [square[0] - 1, square[1] - 1],
            [square[0] - 1, square[1] - 1],
            [square[0] + 1, square[1] - 1],
            [square[0] + 1, square[1] + 1],
        ]
        neighbor_loc = [i for i in neighbor_loc if i not in items_to_remove]
        # neighbor_loc = [i for i in neighbor_loc if tray[i[0]][i[1]] == False]
        squares_list_neighbor.append(neighbor_loc)
    return squares_list_neighbor


def reachable(tray: np.ndarray, square_start: List, square_end: List) -> List:

    path_found = False
    queue = []
    results = []
    visited = set()
    parent = dict()
    parent[tuple(square_start)] = None
    visited.add(tuple(square_start))
    queue.append(tuple(square_start))
    while queue:
        current_square = queue.pop(0)
        if current_square[0] == square_end[0] and current_square[1] == square_end[1]:
            path_found = True
            break
        adjacent_square = neighbors_case_1(tray, current_square)
        for next_square in adjacent_square:
            if next_square not in visited:
                queue.append(next_square)
                parent[next_square] = current_square
                visited.add(next_square)

    if path_found == True:
        results.append(square_end)
        while parent[tuple(square_end)] is not None:
            results.append(parent[tuple(square_end)])
            square_end = parent[tuple(square_end)]
        results.reverse()
    return results


def path(tray: np.ndarray, square_start: List, square_end: List) -> bool:
    if reachable(tray, square_start, square_end):
        results = reachable(tray, square_start, square_end)
        print(f"Path {results}")
        return True
    else:
        return False


if __name__ == "__main__":

    tray = np.array(
        [
            [True, False, False, False],
            [False, True, True, False],
        ]
    )

    square = [0, 2]

    square_neighbor = neighbors_case_1(tray, square)

    squares_list = [[0, 1], [0, 2]]
    squares_list_neighbor = neighbors_case_2(tray, squares_list)

    square_start = [1, 3]
    square_end = [0, 1]
    results = []
    reachable(tray, square_start, square_end)
    if path(tray, square_start, square_end):
        print("Path found!")
    else:
        print("Cannot find path!")
