import random

miles_traveled = 0
thirst = 0
camel_tiredness = 0
natives_distance = -20
drinks = 3
enemies = 0

print("Welcome to Camel!")
print("You have stolen a camel to make your way across the great Mobi desert.")
print("The natives want their camel back and are chasing you down! Survive your")
print("desert trek and out run the natives.")

done = False

while not done:
    oasis = random.randrange(20)
    if oasis == 1 and not done:
        print("\n-----> You found an oasis!")
        print("You drink some water, refill your canteen and take a nap")
        drinks = 3
        thirst = 0
        camel_tiredness = 0

    print("\nA. Drink from your canteen.")
    print("B. Ahead moderate speed.")
    print("C. Ahead full speed.")
    print("D. Stop for the night.")
    print("E. Status check.")
    print("Q. Quit.")

    user_choice = input("What is your choice? ")

    if user_choice.upper() == "Q":
        print("\nAww you quit :(")
        done = True

    elif user_choice.upper() == "A":
        # DRINK FROM CANTEEN
        if drinks > 0:
            drinks -= 1
            thirst = 0
            print("\nYou feel refreshed.")
        else:
            print("\nError 404 \nThere's no water...")
        print("A")

    elif user_choice.upper() == "B":
        # AHEAD MODERATE SPEED
        miles_traveled += random.randrange(5, 10)
        thirst += 1
        camel_tiredness += 1
        natives_distance += random.randrange(7, 15)
        print("\nYou are now", miles_traveled - natives_distance, "miles ahead of natives")

    elif user_choice.upper() == "C":
        # AHEAD FULL SPEED
        miles_traveled += random.randrange(10, 18)
        thirst += 1
        camel_tiredness += random.randrange(1, 4)
        natives_distance += random.randrange(7, 15)
        print("\nYou are now", miles_traveled - natives_distance, "miles ahead of natives")

    elif user_choice.upper() == "D":
        # STOP FOR THE NIGHT
        camel_tiredness = 0
        natives_distance += random.randrange(7, 15)
        print("\nCamel is happy :)")
        print("Drinks in canteen:", drinks)
        print("The natives are", miles_traveled - natives_distance, "miles behind you")

    elif user_choice.upper() == "E":
        # STATUS CHECK
        print("\nMiles traveled:", miles_traveled)
        print("Drink in canteen:", drinks)
        print("The natives are", miles_traveled - natives_distance, "miles behind you")

    if thirst > 6:
        print("\nYour died of thirst...")
        done = True
    elif thirst > 4 and done is False:
        print("\n-----> You are thirsty!")

    if camel_tiredness > 8:
        print("\nYour camel is died of tiredness...")
        done = True
    elif camel_tiredness > 5 and done is False:
        print("\n-----> Your camel is getting tired!")

    enemies = miles_traveled - natives_distance

    if enemies <= 0:
        print("\nThe natives have caught up to you and took you captive")
        done = True
    elif enemies < 15 and done is False:
        print("\n-----> Quick! The natives are getting close!")

    if miles_traveled >= 200 and not done:
        print("\nYay! You out ran the natives and won the game!")
        done = True
