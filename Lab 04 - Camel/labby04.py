import random

miles_traveled = 0
thirst = 0
camel_tiredness = 0
distance_natives_traveled = -20
drinks_nr = 3

print("Welcome to Camel!")
print("You have stolen a camel to make your way across the great Mobi desert.")
print("The natives want their camel back and are chasing you down! Survive your")
print("desert trek and out run the natives.")

done = False

while not done:
    random_oasis = 0
    print("\nA. Drink from your canteen.")
    print("B. Ahead moderate speed.")
    print("C. Ahead full speed.")
    print("D. Stop for the night.")
    print("E. Status check.")
    print("Q. Quit.")

    user_choice = input("What is your choice? ")

    rand_native_distance = random.randrange(7, 14)
    rand_full_distance = random.randrange(10, 20)
    rand_moderate_distance = random.randrange(5, 12)

    if user_choice.upper() == "Q":
        # QUITING
        done = True
        print("\nOh no! You quit the game... I guess it's goodbye then :((((( ")

    elif user_choice.upper() == "A":
        # DRINK FROM CANTEEN
        if drinks_nr > 0:
            drinks_nr -= 1
            thirst = 0
            print("You feel refreshed.")
        else:
            print("Error 404 \nThere's no water")

    elif user_choice.upper() == "B":
        # AHEAD MODERATE SPEED
        miles_traveled += rand_moderate_distance
        print("\nMiles traveled: " + str(miles_traveled))
        thirst += 1
        camel_tiredness += 1
        distance_natives_traveled += rand_native_distance
        random_oasis = random.randrange(20)

    elif user_choice.upper() == "C":
        # AHEAD FULL SPEED
        miles_traveled += rand_full_distance
        print("\nMiles traveled: " + str(miles_traveled))
        thirst += 1
        camel_tiredness += random.randrange(1, 3)
        distance_natives_traveled += rand_native_distance
        random_oasis = random.randrange(20)

    elif user_choice.upper() == "D":
        # STOP FOR THE NIGHT
        camel_tiredness = 0
        print("\nThe camel is happy! :)")
        distance_natives_traveled += rand_native_distance

    elif user_choice.upper() == "E":
        # STATUS CHECK
        print("\nMiles traveled: " + str(miles_traveled))
        print("Drinks in canteen: " + str(drinks_nr))
        print("The natives are " + str(miles_traveled - distance_natives_traveled) + " miles behind you")
        print("")

random_oasis = random.randrange(1, 21)
if random_oasis == 20:
    drinks_nr = 3
    thirst = 0
    camel_tiredness = 0
    print("You found an oasis")

if thirst > 6:
    print("Your camel died of thirst")
    done = True
elif thirst > 4:
    print("You are thirsty")

if drinks_nr > 0:
    drinks_nr -= 1
    thirst = 0
    print("You feel refreshed.")
else:
    print("Error 404 \nThere's no water")

distance_between = miles_traveled - distance_natives_traveled
if distance_between <= 0:
    print("The natives have caught you!")
    done = True
elif distance_between < 15:
    print("The natives are getting close!")

if miles_traveled >= 200 and not done:
    done = True
    print("Yay! You out ran the natives and won the game!")
