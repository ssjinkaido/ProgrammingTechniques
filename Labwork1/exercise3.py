def display_pattern_one(rows: int) -> None:
    for i in range(rows):
        for j in range(0, i + 1):
            print("*", end="")
        print("")


def display_pattern_second(rows: int) -> None:
    for i in range(1, rows + 1):
        for j in range(rows, i, -1):
            print(end=" ")
        for k in range(1, i * 2):
            print("*", end="")
        print(" ")


if __name__ == "__main__":
    rows = int(input("Enter number of rows: "))
    while rows < 1:
        rows = int(input("Enter number of rows: "))
    display_pattern_one(rows)
    print("\n")
    display_pattern_second(rows)
