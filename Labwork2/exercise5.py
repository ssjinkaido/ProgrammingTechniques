from typing import List


def check_symmetry(random_list: List) -> None:
    n = len(random_list)
    flag = 0
    if n % 2:
        mid = n // 2 + 1
    else:
        mid = n // 2

    start1 = 0
    start2 = mid

    while start1 < mid and start2 < n:

        if random_list[start1] == random_list[start2]:
            start1 += 1
            start2 += 1
        else:
            flag = 1
            break
    if flag == 0:
        print("The list is symmetrical")
    else:
        print("The list is not symmetrical")


if __name__ == "__main__":
    random_list = [5, 6, 7, 5, 6, 7]
    print(f"Random list: {random_list}")
    check_symmetry(random_list)
