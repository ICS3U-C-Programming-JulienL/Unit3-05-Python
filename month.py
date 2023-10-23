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
            print("{} represents January.".format(month_number))

        case 2:
            print("{} represents February.".format(month_number))

        case 3:
            print("{} represents March.".format(month_number))

        case 4:
            print("{} represents April.".format(month_number))

        case 5:
            print("{} represents May.".format(month_number))

        case 6:
            print("{} represents June.".format(month_number))

        case 7:
            print("{} represents July.".format(month_number))

        case 8:
            print("{} represents August.".format(month_number))

        case 9:
            print("{} represents September.".format(month_number))

        case 10:
            print("{} represents October.".format(month_number))

        case 11:
            print("{} represents November.".format(month_number))

        case 12:
            print("{} represents December.".format(month_number))
            
        case _:
            # if the user enters an invalid number, tell them to enter a number between 1 and 12
            print("Please enter an integer between 1 and 12.")


1

if __name__ == "__main__":
    main()
