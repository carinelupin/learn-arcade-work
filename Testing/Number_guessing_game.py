"""
Random Number Guessing Game
"""
import random


def main():

    print("Hi! I'm thinking of a random number between 1 & 100.")

    # Create secret number
    secret_nr = random.randrange(1, 101)

    # Initialise our attempt count, we start w attempt 1
    user_attempt_nr = 1

    # set user guess to something secret nr can't be
    # s we can get our 'while' loop started
    user_guess = 0

    # loop until user guess our secret nr / we run out of attempts
    while user_guess != secret_nr and user_attempt_nr < 8:

        # Tell user what attempt we are on & get their guess:
        print("--- Attempt", user_attempt_nr)
        user_input_txt = input("Guess what nr I am thinking of: ")
        user_guess = int(user_input_txt)

        # print if we're too high / low / we got it
        if user_guess > secret_nr:
            print("Too high")
        elif user_guess < secret_nr:
            print("Too low")
        else:
            print("You got it!!!")

        # add to attempt count
        user_attempt_nr += 1

    # here check to see if user didn't guess answer & ran out of tries
    # let them know what nr was
    if user_guess != secret_nr:
        print("Aw man, you ran out of tries... The nr was " + str(secret_nr) + ".")


main()
