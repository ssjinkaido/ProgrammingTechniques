import random


def roll_dice_one(dice_first: int, dice_second: int) -> None:
    print(f"dice first: {dice_first}, dice second: {dice_second}")
    if dice_first == 6 and dice_second == 6:
        print("We have two six, we don't need to restart")
    elif dice_first == 6:
        print("Dice first get six, restart dice second")
    elif dice_second == 6:
        print("Dice second get six, restart dice first")
    else:
        print("Restart both dices")


def roll_dice_second(dice_first: int, dice_second: int) -> bool:
    if (dice_first == 6) and (dice_second == 6):
        print(f"dice first: {dice_first}, dice second: {dice_second}")
        return True
    else:
        print(f"dice first: {dice_first}, dice second: {dice_second}")
        print("Roll the dice again")
        return False


if __name__ == "__main__":
    two_six = False
    dice_first = random.randint(0, 6)
    dice_second = random.randint(0, 6)
    roll_dice_one(dice_first, dice_second)

    while not two_six:
        dice_first = random.randint(0, 6)
        dice_second = random.randint(0, 6)
        if roll_dice_second(dice_first, dice_second):
            two_six = True
        else:
            two_six = False
