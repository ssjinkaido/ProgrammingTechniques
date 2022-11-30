from typing import List


def check_prime_number(num: int) -> bool:
    if num == 2:
        return True
    elif num < 2:
        return False
    else:
        for i in range(2, num // 2 + 1):
            if num % i == 0:
                return False
        return True


def print_first_prime_numbers(list_numbers: List) -> None:
    for i in range(len(list_numbers)):
        if check_prime_number(i):
            print(f"First prime number is {list_numbers[i]}")
            break


if __name__ == "__main__":
    num = int(input("Enter a number: "))
    if check_prime_number(num) == True:
        print(f"{num} is prime")
    else:
        print(f"{num} is not prime")
    list_numbers = [6, 8, 3, 5, 7]
    print_first_prime_numbers(list_numbers)
