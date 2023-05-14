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
        else:
            print("Error 404 \nThere's no water")

    elif user_choice.upper() == "B":
        # AHEAD MODERATE SPEED
        miles_traveled += rand_moderate_distance
        print("\nMiles traveled: " + str(miles_traveled))
        thirst += 1
        camel_tiredness += 1
        distance_natives_traveled += rand_native_distance

    elif user_choice.upper() == "C":
        # AHEAD FULL SPEED
        miles_traveled += rand_full_distance
        print("\nMiles traveled: " + str(miles_traveled))
        thirst += 1
        camel_tiredness += random.randrange(1, 3)
        distance_natives_traveled += rand_native_distance

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


if thirst >= 4:
    print("You are thirsty")
elif thirst >= 6:
    done = True
    print("Your camel died of thirst")

if camel_tiredness >= 5:
    print("Your camel is getting tired")
elif camel_tiredness >= 8:
    done = True
    print("")
