# Created by Dylan Melo
# Created on December 2021
# This program gets the user to enter length and width of a rectangle
# and it will tell them if it is or is not a square.
import colorama
from colorama import Fore
from colorama import Style


def main():
    # get user length, width and unit.
    colorama.init()
    print(Fore.RED + Style.BRIGHT + "Today we will tell you if")
    print(Fore.GREEN + Style.BRIGHT + "your rectangle is a square!")
    length_string = input(Fore.YELLOW + Style.BRIGHT + "Enter the length: ")
    try:
        length = float(length_string)
    except Exception:
        print("Your input was not a number")
        quit()
    width_string = input(Fore.GREEN + Style.BRIGHT + "Enter the width: ")
    try:
        width = float(width_string)
    except Exception:
        print("Your input was not a number")
        quit()

    # Process if length and width are equal it is a square.

    if length == width:
        print(Fore.RED + Style.BRIGHT + "Your rectangle is a square")
    else:
        print(Fore.RED + Style.BRIGHT + "Your rectangle is not a square")


if __name__ == "__main__":
    main()
