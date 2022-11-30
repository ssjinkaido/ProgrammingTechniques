import random
from typing import List


def create_list() -> List:
    random_list = random.sample(range(1, 1000), random.randint(2, 10))
    return random_list


def check_palindrome(random_list: List) -> None:
    n = len(random_list)
    flag = 0
    if n % 2:
        mid = n // 2 + 1
    else:
        mid = n // 2

    start = 0
    last = n - 1

    while start <= mid:

        if random_list[start] == random_list[last]:
            start += 1
            last -= 1
        else:
            flag = 1
            break
    if flag == 0:
        print("The string is palindrome")
    else:
        print("The string is not palindrome")


if __name__ == "__main__":
    random_string = "abcxyzyxcba"
    print(f"Random list: {random_string}")
    check_palindrome(random_string)
