import math


def solve_equation(a: float, b: float, c: float) -> None:
    discriminant = b * b - 4 * a * c
    square_root_discriminant = math.sqrt(abs(discriminant))
    if discriminant > 0:
        print("The equation has two real roots")
        root_one = (-b + square_root_discriminant) / (2 * a)

        root_two = (-b - square_root_discriminant) / (2 * a)
        print(f"Root one: {root_one:.4f}, root two: {root_two:.4f}")

    elif discriminant == 0:
        print("The equation has 2 same roots")
        root_one = -b / (2 * a)
        root_two = -b / (2 * a)
        print(f"root one: {root_one:.4f}, root two: {root_two:.4f}")

    else:
        print("The equation has no real roots")


if __name__ == "__main__":
    a = float(input("Enter a: "))
    b = float(input("Enter b: "))
    c = float(input("Enter c: "))
    solve_equation(a, b, c)
