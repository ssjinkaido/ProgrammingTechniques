import random
from typing import List


def create_list() -> List:
    random_list = random.sample(range(1, 1000), random.randint(5, 100))
    return random_list


def repeat(word, n)->str:
    return (f"{word} " * n)[:-1]


def solve_task(random_list: List) -> None:
    print(f"The fifth value of the list is: {random_list[4]}")
    random_list[1] = 17
    random_list[3] = random_list[2] + random_list[4]
    print(f"Display the value of the last term of the list 12 times: ")
    print(repeat(random_list[-1], 12))


if __name__ == "__main__":
    random_list = create_list()
    solve_task(random_list)
