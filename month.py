#!/usr/bin/env python3

# Created By: Julien Lamoureux
# Date: October 23, 2023
# This program is used to show numbers represented as months


def main():
    # get the user integer
    month_number = int(
        input(
            "This program is used to show  numbers represented as months (1 being January, 2 being February, etc.). Enter a number: "
        )
    )

    # use a match case to show what numbers the months are represented by
    match month_number:
        case 1:
            print("1 represents January.")

        case 2:
            print("2 represents February.")

        case 3:
            print("3 represents March.")

        case 4:
            print("4 represents April.")

        case 5:
            print("5 represents May.")

        case 6:
            print("6 represents June.")

        case 7:
            print("7 represents July.")

        case 8:
            print("8 represents August.")

        case 9:
            print("9 represents September.")

        case 10:
            print("10 represents October.")

        case 11:
            print("11 represents November.")

        case 12:
            print("12 represents December.")
        case _:
            print("Please enter an integer between 1 and 12.")
1

if __name__ == "__main__":
    main()
