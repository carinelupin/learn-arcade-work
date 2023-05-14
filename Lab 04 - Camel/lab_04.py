import random

miles_traveled = 0
thirst = 0
camel_tiredness = 0
distance_natives_traveled = -20
drinks_nr = 3


def main():
    print("Welcome to Camel!")
    print("You have stolen a camel to make your way across the great Mobi desert.")
    print("The natives want their camel back and are chasing you down! Survive your")
    print("desert trek and out run the natives.")
    print("")

    done = False
    while not done:
        print("A. Drink from your canteen.")
        print("B. Ahead moderate speed.")
        print("C. Ahead full speed.")
        print("D. Stop for the night.")
        print("E. Status check.")
        print("Q. Quit.")

        user_choice = input("What is your choice? ")

        if user_choice.upper() == "Q":
            done = True
            print("")
            print("Oh no! You quit the game... I guess it's goodbye then :((((( ")
        elif user_choice.upper() == "E":
            print("")
            print("Miles traveled: " + str(miles_traveled))
            print("Drinks in canteen: " + str(drinks_nr))
            print("The natives are " + str(miles_traveled - distance_natives_traveled) + " miles behind you")
            print("")
        elif user_choice.upper() == "D":

            print("")
            print("The camel is happy")


main()
