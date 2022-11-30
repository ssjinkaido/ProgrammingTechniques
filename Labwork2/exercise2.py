import random
from typing import List


def create_list() -> List:
    random_list = random.sample(range(1, 1000), random.randint(2, 10))
    return random_list


def display_list_in_column(random_list: List) -> None:
    rows = len(random_list)
    for num in random_list:
        for col in range(1):
            print(num, "\t", end="")
        print()


def count_multiple_of_threes(random_list: List) -> None:
    count = 0
    for num in random_list:
        if num % 3 == 0:
            count += 1
    print(f"The number of multiple of 3 in the list is: {count}")


def count_even_values(random_list: List) -> None:
    sum_even = 0
    for num in random_list:
        if num % 2 == 0:
            sum_even += num
    print(f"The sum of even values in the list is: {sum_even}")


def find_maximum_and_minimum(random_list: List) -> None:
    print(
        f"The maximum value is {max(random_list)}, the minimum value is: {min(random_list)}"
    )


def calculate_mean(random_list: List) -> None:
    mean_larger_than_10 = False
    mean_list = sum(random_list) / len(random_list)
    if mean_list >= 10:
        mean_larger_than_10 = True
        print("The mean is greater or equal to 10")
    else:
        print("The mean is smaller than 10")
        mean_larger_than_10 = False


def calculate_product_between_intervals(random_list: List) -> None:
    product_interval = 1
    for num in random_list:
        if num <= 70 and num >= 50:
            product_interval *= num
    if product_interval == 1:
        product_interval = 0
    print(f"The product is: {product_interval}")


def display_list_in_reverse(random_list: List) -> None:
    length_list = len(random_list)
    for i in range(length_list - 1, -1, -1):
        print(f"List at index {i} {random_list[i]}", "\t")


if __name__ == "__main__":
    random_list = create_list()
    display_list_in_column(random_list)
    count_multiple_of_threes(random_list)
    count_even_values(random_list)
    find_maximum_and_minimum(random_list)
    calculate_mean(random_list)
    calculate_product_between_intervals(random_list)
    display_list_in_reverse(random_list)
