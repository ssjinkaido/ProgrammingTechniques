import random
from typing import List


def create_list() -> List:
    random_list = random.sample(range(1, 1000), random.randint(5, 100))
    return random_list


def swap_values(random_list: List) -> List:
    random_list[0], random_list[-1] = random_list[-1], random_list[0]
    return random_list


if __name__ == "__main__":
    random_list = create_list()
    print(f"List before swap values: {random_list}")
    list_after_swap = swap_values(random_list)
    print(f"List after swap values: {list_after_swap}")
