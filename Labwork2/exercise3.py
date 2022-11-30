import string
import random


def get_random_string(length) -> str:
    letters = string.ascii_lowercase
    random_string = "".join(random.choice(letters) for i in range(length))
    print("Random string of length", length, "is:", random_string)
    return random_string


def create_dictionary(random_string: str) -> None:
    dict_string = {}
    for i in random_string:
        if i in dict_string:
            dict_string[i] += 1
        else:
            dict_string[i] = 1
    for key, value in dict_string.items():
        print(f"The number of occurences of {key} in the string is {value}")


if __name__ == "__main__":
    count_occurences = 0
    random_string = get_random_string(random.randint(1, 10))
    create_dictionary(random_string)
    random_character = random.choice(string.ascii_lowercase)
    for i in random_string:
        if i == random_character:
            count_occurences += 1
    print("")
    print(f"The number of occurrences of {random_character} is {count_occurences}")
