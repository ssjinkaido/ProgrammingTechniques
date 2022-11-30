def terms(n: int) -> int:
    if n == 0:
        return 1
    elif n > 0:
        if (terms(n - 1) % 2) == 0:
            return -terms(n - 1) + 3
        else:
            return -terms(n - 1) * 3 + 1


if __name__ == "__main__":
    n = int(input("Enter n: "))
    list_terms = []
    for i in range(n + 1):
        print(f"{i}th rank: {terms(i)}")
